#!/usr/bin/env python3
"""
Generates the comprehensive data file for NCERT Class 7 Mathematics:
Chapter 5: Connecting the Dots... (Data Handling & Statistics)
Contains 20 slides, 32 checkpoints, and 40 quiz questions with step-by-step solutions.
"""

import json

SLIDES_DATA = [
    # Slide 1
    {
        "slide_num": 1,
        "badge": "Section 5.1",
        "section": "Of Questions and Statements",
        "title": "The Art of Statistical Thinking",
        "sim_id": "sim-questions-classifier",
        "narration": "Welcome, young researchers! I am Professor P. C. Mahalanobis. In science and life, everything begins with how we ask questions. Today, let us discover what makes a question truly statistical!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl">
    <h4 class="font-bold text-indigo-300 text-sm mb-1">🔍 What is a Statistical Question?</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      Not every question is a statistical question. A <b>statistical question</b> is one that anticipates <b>variability</b> in the data collected to answer it. If a question has a single deterministic fact as its answer, it is non-statistical.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-rose-500/30">
      <div class="font-bold text-rose-300 mb-1">❌ Non-Statistical (Fixed Single Answer)</div>
      <ul class="space-y-1.5 text-slate-300 list-disc list-inside">
        <li>"How tall is Mount Everest?" (Fixed: $8848.86\text{ m}$)</li>
        <li>"What is the capital of India?" (New Delhi)</li>
        <li>"How many days are in a leap year?" ($366\text{ days}$)</li>
      </ul>
      <p class="mt-2 text-[11px] text-slate-400">No data collection or variability required—just look up one factual value.</p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-emerald-500/30">
      <div class="font-bold text-emerald-300 mb-1">✓ Statistical (Anticipates Variability)</div>
      <ul class="space-y-1.5 text-slate-300 list-disc list-inside">
        <li>"How tall are Class 7 students in our school?" (Varies across students)</li>
        <li>"How much time do students spend on homework daily?" (Varies by day & person)</li>
        <li>"What are the monthly prices of onions in Delhi?" (Fluctuates across months)</li>
      </ul>
      <p class="mt-2 text-[11px] text-slate-400">Requires collecting data across many units and analyzing distribution patterns.</p>
    </div>
  </div>

  <div class="p-3 bg-amber-500/10 border border-amber-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-amber-300">Key Takeaway:</span> Statistical thinking begins whenever we acknowledge that the real world is filled with diversity, fluctuations, and natural spread.
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Which of the following is a genuine statistical question?",
                "options": [
                    "How many legs does a spider have?",
                    "What was the temperature in Chennai at noon yesterday?",
                    "How many books do students in your school read per month?",
                    "What is 15 × 12?"
                ],
                "correct": 2,
                "explanation": "The number of books read per month varies from student to student, requiring data collection across individuals."
            },
            {
                "question": "Why is 'How old is the school principal?' NOT a statistical question?",
                "options": [
                    "Because it is an impolite question",
                    "Because it has a single fixed factual answer with no variability",
                    "Because age cannot be measured in numbers",
                    "Because statistical questions only deal with money"
                ],
                "correct": 1,
                "explanation": "A single person's current age has one specific value at any given moment; there is no variability or data distribution to analyze."
            }
        ]
    },

    # Slide 2
    {
        "slide_num": 2,
        "badge": "Section 5.1",
        "section": "Of Questions and Statements",
        "title": "Statistical Statements & Evidence",
        "sim_id": "sim-statements-analyzer",
        "narration": "In newspapers, sports broadcasts, and science reports, we encounter statements made with numbers. Let us learn how to dissect claims, proportions, and predictions like a true statistician!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-cyan-500/10 border border-cyan-500/30 rounded-xl">
    <h4 class="font-bold text-cyan-300 text-sm mb-1">📰 Decoding Statistical Statements</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      A <b>statistical statement</b> makes a claim based on aggregate numerical evidence, proportions, or probabilistic forecasts rather than absolute certainty.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-teal-300 mb-1">1. Summary Claims</div>
      <p class="text-slate-300">
        "On average, children in Town A sleep $8.5\text{ hours}$ each night."<br>
        <i>Nature:</i> Summarizes an entire population with a central representative value.
      </p>
    </div>
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-amber-300 mb-1">2. Proportional Claims</div>
      <p class="text-slate-300">
        "Three out of four households in the village use solar energy."<br>
        <i>Nature:</i> Communicates relative frequency ($\frac{3}{4} = 75\%$) rather than raw counts.
      </p>
    </div>
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-purple-300 mb-1">3. Predictive Statements</div>
      <p class="text-slate-300">
        "There is an $80\%$ chance of monsoon showers tomorrow afternoon."<br>
        <i>Nature:</i> Quantifies uncertainty based on past historical weather models.
      </p>
    </div>
  </div>

  <div class="p-3 bg-slate-900/60 rounded-xl border border-slate-700/50 text-xs text-slate-300 space-y-1">
    <b class="text-emerald-400">The Skeptical Reader's Checklist:</b>
    <div>1. <i>Who was measured?</i> (Sample size and representation)</div>
    <div>2. <i>How was it measured?</i> (Objective measurement vs subjective opinion)</div>
    <div>3. <i>Is the claim supported by underlying data?</i></div>
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "A news report states: '40% of surveyed families own a bicycle.' What type of statistical claim is this?",
                "options": [
                    "A deterministic mathematical proof",
                    "A proportional relative frequency statement",
                    "A non-statistical superstition",
                    "An absolute count of all bicycles in the country"
                ],
                "correct": 1,
                "explanation": "40% expresses a proportional ratio of families with bicycles relative to the total surveyed sample."
            },
            {
                "question": "If a weather report says '70% chance of rain', what does this indicate?",
                "options": [
                    "It will rain on exactly 70% of the surface area of your shirt",
                    "It will definitely rain for exactly 7 hours",
                    "Under similar atmospheric conditions in the past, rain occurred 7 out of 10 times",
                    "Rain is 100% impossible"
                ],
                "correct": 2,
                "explanation": "Probability in weather statements quantifies historical frequency under matching atmospheric data."
            }
        ]
    },

    # Slide 3
    {
        "slide_num": 3,
        "badge": "Section 5.2",
        "section": "Representative Values",
        "title": "Representative Values & The Fair Share",
        "sim_id": "sim-fair-share-balancer",
        "narration": "Imagine four friends collect 12, 8, 14, and 6 marbles. How do we represent this group with a single fair number? In ancient India, this concept was known as samamiti or samīkaraṇa—the beauty of equal leveling!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-amber-500/10 border border-amber-500/30 rounded-xl">
    <h4 class="font-bold text-amber-300 text-sm mb-1">⚖️ The Concept of Representative Value</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      When we have a collection of diverse numbers, our brains struggle to hold all details at once. A <b>representative value</b> is a single central number that summarizes the general magnitude of the entire group.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-cyan-300 mb-1">The "Fair Share" Physical Model</div>
      <p class="text-slate-300 leading-relaxed">
        Imagine columns of wooden blocks of heights $12$, $8$, $14$, and $6$.
      </p>
      <div class="my-2 p-2 bg-slate-900/60 rounded border border-slate-700/40 text-center font-mono text-amber-200">
        Total Blocks = $12 + 8 + 14 + 6 = 40$ blocks<br>
        Distributed equally among 4 columns: $\frac{40}{4} = \mathbf{10\text{ blocks each}}$
      </div>
      <p class="text-slate-400">
        Taking from towers with surplus and giving to towers with deficit levels them all to a uniform height of $10$.
      </p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-emerald-300 mb-1">Heritage: <i>Samamiti</i> & <i>Samīkaraṇa</i></div>
      <p class="text-slate-300 leading-relaxed">
        In traditional Indian arithmetic treatises, the concept of leveling unequal distributions was called <b>Samīkaraṇa</b> (making things equal) and <b>Samamiti</b> (equalized measure).
      </p>
      <p class="text-slate-400 mt-2">
        It formalizes the moral and practical impulse of equitable distribution: pooling resources into one common vessel and sharing equally among all contributors.
      </p>
    </div>
  </div>

  <div class="p-3 bg-teal-500/10 border border-teal-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-teal-300">Definition:</span> The <b>Arithmetic Mean</b> (or average) is the value each individual item would receive if the total sum were redistributed equally.
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Three glasses have 150 mL, 200 mL, and 250 mL of fruit juice. If shared equally, how much does each glass hold?",
                "options": ["180 mL", "200 mL", "210 mL", "225 mL"],
                "correct": 1,
                "explanation": "Total juice = 150 + 200 + 250 = 600 mL. Shared equally among 3 glasses = 600 / 3 = 200 mL."
            },
            {
                "question": "What does the Sanskrit mathematical term 'Samīkaraṇa' signify in the context of averages?",
                "options": [
                    "Subtracting prime numbers",
                    "Making quantities equal or leveling out differences",
                    "Multiplying by powers of ten",
                    "Calculating triangle angles"
                ],
                "correct": 1,
                "explanation": "Samīkaraṇa literally means 'making equal'—redistributing uneven values into identical fair shares."
            }
        ]
    },

    # Slide 4
    {
        "slide_num": 4,
        "badge": "Section 5.2",
        "section": "Representative Values",
        "title": "Computing the Arithmetic Mean",
        "sim_id": "sim-mean-balance-beam",
        "narration": "To calculate the mean of any dataset, we divide the sum of all observations by the total number of observations. Physically, the mean acts as the balance fulcrum of a seesaw!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl">
    <h4 class="font-bold text-indigo-300 text-sm mb-1">📐 The Mathematical Formula for Mean</h4>
    <div class="my-2 p-2 bg-slate-900/60 rounded-lg text-center font-mono text-cyan-200">
      $$\text{Arithmetic Mean} = \frac{\text{Sum of all observations}}{\text{Number of observations}} = \frac{\sum x_i}{n}$$
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-amber-300 mb-1">Step-by-Step Calculation</div>
      <p class="text-slate-300">Find the mean of test scores: $7, 9, 6, 10, 8$</p>
      <ol class="mt-1.5 space-y-1 text-slate-300 list-decimal list-inside">
        <li>Count observations: $n = 5$</li>
        <li>Compute sum: $7 + 9 + 6 + 10 + 8 = 40$</li>
        <li>Divide: $\text{Mean} = \frac{40}{5} = \mathbf{8}$</li>
      </ol>
      <p class="mt-2 text-slate-400">Notice the mean ($8$) lies comfortably between the minimum ($6$) and maximum ($10$).</p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-emerald-300 mb-1">The Fulcrum / Balance Model</div>
      <p class="text-slate-300">
        If you place weights along a ruler at their coordinate values, the <b>Arithmetic Mean</b> is the exact fulcrum point where the ruler balances horizontally without tilting!
      </p>
      <p class="text-slate-400 mt-2">
        The sum of distances of values to the left of the mean exactly equals the sum of distances of values to the right:
        $$\sum (x_i - \text{Mean}) = 0$$
      </p>
    </div>
  </div>

  <div class="p-3 bg-rose-500/10 border border-rose-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-rose-300">Vital Property:</span> The mean does not have to be one of the original numbers in the dataset! For example, the mean of $4$ and $5$ is $4.5$, even though neither item was $4.5$.
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the arithmetic mean of 12, 18, 20, 14, and 16?",
                "options": ["15", "16", "17", "18"],
                "correct": 1,
                "explanation": "Sum = 12 + 18 + 20 + 14 + 16 = 80. Total numbers n = 5. Mean = 80 / 5 = 16."
            },
            {
                "question": "A cricket batsman scores 40, 50, 60, and 70 runs in four matches. What must he score in the 5th match to achieve an average of 60 runs?",
                "options": ["60 runs", "70 runs", "80 runs", "90 runs"],
                "correct": 2,
                "explanation": "For 5 matches with mean 60, target sum = 5 × 60 = 300 runs. Current sum = 40 + 50 + 60 + 70 = 220 runs. Required score = 300 - 220 = 80 runs."
            }
        ]
    },

    # Slide 5
    {
        "slide_num": 5,
        "badge": "Section 5.2",
        "section": "Representative Values",
        "title": "Know Your Onions! Town A vs Town B",
        "sim_id": "sim-onion-comparator",
        "narration": "In the NCERT chapter, we meet a classic real-world puzzle: tracking monthly onion prices in Town A and Town B. Let's see how minimum, maximum, total, and range help us compare them!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-purple-500/10 border border-purple-500/30 rounded-xl">
    <h4 class="font-bold text-purple-300 text-sm mb-1">🧅 The Onion Price Mystery</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      Suppose two towns record their monthly onion prices per kg over a 6-month period. Can the mean alone tell the whole story? Let us examine the actual numbers!
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-blue-500/30">
      <div class="font-bold text-blue-300 mb-1">Town A (Stable Supply)</div>
      <p class="text-slate-300 font-mono">₹28, ₹30, ₹32, ₹29, ₹31, ₹30</p>
      <ul class="mt-2 space-y-1 text-slate-300">
        <li>• Minimum: $\text{Rs. } 28$</li>
        <li>• Maximum: $\text{Rs. } 32$</li>
        <li>• Range: $32 - 28 = \mathbf{4}$</li>
        <li>• Total: $180 \implies \text{Mean} = \frac{180}{6} = \mathbf{30}$</li>
      </ul>
      <p class="mt-2 text-[11px] text-blue-400">Low spread, dependable and predictable pricing.</p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-amber-500/30">
      <div class="font-bold text-amber-300 mb-1">Town B (Volatile Supply)</div>
      <p class="text-slate-300 font-mono">₹10, ₹15, ₹20, ₹45, ₹60, ₹30</p>
      <ul class="mt-2 space-y-1 text-slate-300">
        <li>• Minimum: $\text{Rs. } 10$</li>
        <li>• Maximum: $\text{Rs. } 60$</li>
        <li>• Range: $60 - 10 = \mathbf{50}$</li>
        <li>• Total: $180 \implies \text{Mean} = \frac{180}{6} = \mathbf{30}$</li>
      </ul>
      <p class="mt-2 text-[11px] text-amber-400">Extreme volatility—huge spike during shortages!</p>
    </div>
  </div>

  <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl text-xs text-slate-300">
    <b class="text-indigo-300">Crucial Insight:</b> Both towns have the exact same mean price ($\text{Rs. } 30$), yet their price stability is completely different! We need measures of <b>spread</b> (range and dot plots) alongside the mean.
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the 'Range' of a dataset?",
                "options": [
                    "The average of all values",
                    "The difference between the maximum and minimum observations",
                    "The most frequent number",
                    "The middle number after sorting"
                ],
                "correct": 1,
                "explanation": "Range = Maximum value - Minimum value. It quantifies the total spread of the data."
            },
            {
                "question": "Town A has onion prices ranging from ₹28 to ₹32 (range 4), while Town B ranges from ₹10 to ₹60 (range 50). Which town offers more predictable living expenses?",
                "options": [
                    "Town B because it reached ₹10",
                    "Town A because of its small price range and stability",
                    "Both are identical because both have a mean of ₹30",
                    "Neither town has onions"
                ],
                "correct": 1,
                "explanation": "Town A's small range of ₹4 means consumers experience very little price fluctuation."
            }
        ]
    },

    # Slide 6
    {
        "slide_num": 6,
        "badge": "Section 5.2",
        "section": "Representative Values",
        "title": "Visualising Spread with Dot Plots",
        "sim_id": "sim-dot-plot-generator",
        "narration": "A dot plot is one of the simplest and most visual ways to see data. We place dots along a number line for each observation. Clusters, gaps, and isolated values instantly appear!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-teal-500/10 border border-teal-500/30 rounded-xl">
    <h4 class="font-bold text-teal-300 text-sm mb-1">📍 The Power of Dot Plots</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      A <b>dot plot</b> displays individual observations as stacked dots above a horizontal number line. Every single data point retains its identity—nothing is hidden inside an average formula.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-cyan-300 mb-1">How to Construct a Dot Plot</div>
      <ol class="space-y-1.5 text-slate-300 list-decimal list-inside">
        <li>Draw a horizontal scale covering from minimum to maximum.</li>
        <li>For each observation, place a dot directly above its value.</li>
        <li>If a value repeats, stack dots vertically one above the other.</li>
      </ol>
      <div class="mt-2 text-[11px] text-slate-400">
        Tightly clustered dots indicate high consistency; widely scattered dots indicate high variability.
      </div>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-amber-300 mb-1">What Dot Plots Reveal at a Glance</div>
      <ul class="space-y-1.5 text-slate-300 list-disc list-inside">
        <li><b>Clusters:</b> Where most values bunch together.</li>
        <li><b>Gaps:</b> Empty zones where no observations occurred.</li>
        <li><b>Peaks (Mode):</b> The tallest stack of dots representing the most common value.</li>
        <li><b>Islands:</b> Lonely dots far away from the main cluster (potential outliers).</li>
      </ul>
    </div>
  </div>

  <div class="p-3 bg-slate-900/60 rounded-xl border border-slate-700/50 text-xs text-slate-300">
    <i>Observation:</i> In Town A, all 6 dots cluster within the narrow corridor between $28$ and $32$. In Town B, dots are scattered from $10$ up to $60$.
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "In a dot plot showing daily study hours, the number 2 has 7 stacked dots, and 4 has 2 dots. What does this tell us?",
                "options": [
                    "Studying 4 hours is more popular",
                    "7 students studied for 2 hours, making 2 hours the most common duration (mode)",
                    "Nobody studied for 2 hours",
                    "The mean is exactly 9 hours"
                ],
                "correct": 1,
                "explanation": "The height of the stack directly represents the frequency count of that measurement."
            },
            {
                "question": "What is an empty gap on a dot plot between values 20 and 35 indicative of?",
                "options": [
                    "A drawing mistake by the student",
                    "No observations occurred in the range 20 to 35",
                    "The mean must be zero",
                    "All dots fell off the page"
                ],
                "correct": 1,
                "explanation": "A gap signifies an absence of recorded data values within that numerical interval."
            }
        ]
    },

    # Slide 7
    {
        "slide_num": 7,
        "badge": "Section 5.2",
        "section": "Representative Values",
        "title": "Outliers: When the Mean is Deceived",
        "sim_id": "sim-outlier-disrupter",
        "narration": "What happens if nine workers earn ₹15,000 per month, but the company boss earns ₹5,00,000? The arithmetic mean skyrockets! An extreme value that sits far from the rest is called an outlier.",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-rose-500/10 border border-rose-500/30 rounded-xl">
    <h4 class="font-bold text-rose-300 text-sm mb-1">🚨 The Outlier Trap</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      An <b>outlier</b> is an observation that lies an abnormal distance from other values in a random sample. The Arithmetic Mean is notoriously sensitive to outliers because it incorporates every single numerical value into its numerator.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-amber-300 mb-1">The Small Workshop Example</div>
      <p class="text-slate-300">Monthly salaries of 5 workers in a tailoring shop:</p>
      <div class="p-2 my-1.5 bg-slate-900/60 rounded font-mono text-cyan-200">
        ₹10,000, ₹11,000, ₹10,000, ₹12,000, ₹11,000
      </div>
      <p class="text-slate-300">
        Sum = $\text{Rs. } 54,000 \implies \text{Mean} = \frac{54000}{5} = \mathbf{₹10,800}$.<br>
        This mean reflects typical worker earnings accurately.
      </p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-rose-500/40">
      <div class="font-bold text-rose-300 mb-1">Enter the Owner's Salary!</div>
      <p class="text-slate-300">Now include the owner who draws ₹1,60,000:</p>
      <div class="p-2 my-1.5 bg-slate-900/60 rounded font-mono text-rose-200">
        ₹10,000, ₹11,000, ₹10,000, ₹12,000, ₹11,000, <span class="text-rose-400 font-bold">₹1,60,000</span>
      </div>
      <p class="text-slate-300">
        Sum = $\text{Rs. } 2,14,000 \implies \text{New Mean} = \frac{214000}{6} \approx \mathbf{₹35,667}$!<br>
        Not a single worker earns anywhere close to ₹35,667!
      </p>
    </div>
  </div>

  <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-indigo-300">The Problem:</span> If the owner claims: "The average salary in my workshop is over ₹35,000", it is mathematically true but completely misleading! We need a measure resistant to such distortions.
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "In the dataset [4, 5, 5, 6, 4, 85], which value is an outlier?",
                "options": ["4", "5", "6", "85"],
                "correct": 3,
                "explanation": "85 is far removed from the rest of the numbers which all cluster between 4 and 6."
            },
            {
                "question": "What happens to the arithmetic mean when an unusually high outlier is introduced?",
                "options": [
                    "The mean remains completely unchanged",
                    "The mean is pulled sharply upward towards the outlier",
                    "The mean always becomes negative",
                    "The mean turns into zero"
                ],
                "correct": 1,
                "explanation": "Because the outlier is added into the numerator sum, it inflates the mean upwards."
            }
        ]
    },

    # Slide 8
    {
        "slide_num": 8,
        "badge": "Section 5.2",
        "section": "Representative Values",
        "title": "The Median: The Unshakeable Middle",
        "sim_id": "sim-median-finder",
        "narration": "Meet the Median! By simply arranging all observations in order and picking the exact middle value, the median remains immune to extreme outliers.",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-emerald-500/10 border border-emerald-500/30 rounded-xl">
    <h4 class="font-bold text-emerald-300 text-sm mb-1">🛡️ The Median (Middle Representative)</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      The <b>Median</b> refers to the value of the middle observation when all data points are arranged in ascending or descending order. It divides the dataset into two equal halves: $50\%$ of values lie below it, and $50\%$ lie above it.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-teal-300 mb-1">Case 1: Odd Number of Items ($n$ is odd)</div>
      <p class="text-slate-300">Data: $7, 3, 11, 2, 9$ ($n = 5$)</p>
      <ol class="mt-1 space-y-1 text-slate-300 list-decimal list-inside">
        <li><b>Step 1: Sort:</b> $2, 3, \mathbf{7}, 9, 11$</li>
        <li><b>Step 2: Locate middle:</b> Position $\frac{n+1}{2} = \frac{5+1}{2} = 3\text{rd}$ item.</li>
        <li>$\text{Median} = \mathbf{7}$</li>
      </ol>
      <p class="mt-2 text-slate-400">Even if $11$ was replaced by $1,000,000$, the median would still be $7$!</p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-cyan-300 mb-1">Case 2: Even Number of Items ($n$ is even)</div>
      <p class="text-slate-300">Data: $14, 8, 20, 10, 6, 18$ ($n = 6$)</p>
      <ol class="mt-1 space-y-1 text-slate-300 list-decimal list-inside">
        <li><b>Step 1: Sort:</b> $6, 8, \mathbf{10, 14}, 18, 20$</li>
        <li><b>Step 2: Middle two items:</b> $10$ (3rd) and $14$ (4th).</li>
        <li><b>Step 3: Average the pair:</b> $\frac{10 + 14}{2} = \mathbf{12}$.</li>
      </ol>
      <p class="mt-2 text-slate-400">The median is $12$, sitting squarely in the middle gap.</p>
    </div>
  </div>

  <div class="p-3 bg-amber-500/10 border border-amber-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-amber-300">Crucial Golden Rule:</span> Always <b>SORT</b> the data first before locating the median! Finding the middle of unsorted numbers is a fatal error.
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the median of the scores: 18, 12, 25, 10, 30?",
                "options": ["25", "18", "19", "12"],
                "correct": 1,
                "explanation": "Step 1: Sort ascending: 10, 12, 18, 25, 30. Step 2: The middle (3rd) number is 18."
            },
            {
                "question": "What is the median of the four numbers: 5, 8, 12, 16?",
                "options": ["8", "10", "12", "10.5"],
                "correct": 1,
                "explanation": "Already sorted: 5, 8, 12, 16. Middle two numbers are 8 and 12. Median = (8 + 12) / 2 = 20 / 2 = 10."
            }
        ]
    },

    # Slide 9
    {
        "slide_num": 9,
        "badge": "Section 5.2",
        "section": "Representative Values",
        "title": "Mean vs Median: The Decision Matrix",
        "sim_id": "sim-mean-vs-median",
        "narration": "Should you report the mean or the median? In government policies, real estate, and income reports, choosing the wrong measure distorts reality. Here is the golden rule!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl">
    <h4 class="font-bold text-indigo-300 text-sm mb-1">⚖️ Choosing Between Mean and Median</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      Both are measures of central tendency, but their strengths shine in different statistical landscapes.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-emerald-500/40">
      <div class="font-bold text-emerald-300 mb-1">Use the MEAN when:</div>
      <ul class="space-y-1.5 text-slate-300 list-disc list-inside">
        <li>Data is symmetric without extreme spikes.</li>
        <li>Every single value must contribute to a pooled total.</li>
        <li>Calculating total budgeting requirements (e.g., $100\text{ students} \times \text{mean food weight}$).</li>
        <li>Examples: Student test marks in a standardized exam, daily milk yield of a cow.</li>
      </ul>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-amber-500/40">
      <div class="font-bold text-amber-300 mb-1">Use the MEDIAN when:</div>
      <ul class="space-y-1.5 text-slate-300 list-disc list-inside">
        <li>Data contains extreme outliers or skewness.</li>
        <li>You want to understand what a "typical" member experiences.</li>
        <li>Examples: Household incomes, city house prices, hospital waiting times, onion price spikes.</li>
      </ul>
    </div>
  </div>

  <div class="p-3 bg-slate-900/60 rounded-xl border border-slate-700/50 text-xs text-slate-300">
    <b>Real World Example:</b> When reporting national wealth or income, economists always report the <b>Median Household Income</b> rather than the Mean, because billionaires like Elon Musk or Mukesh Ambani would artificially inflate the mean.
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Which measure of central tendency is preferred when reporting city house prices where a few luxury mansions cost 100 times more than ordinary apartments?",
                "options": ["Arithmetic Mean", "Median", "Maximum", "Range"],
                "correct": 1,
                "explanation": "Median is robust against extreme house prices and reflects what typical families pay."
            },
            {
                "question": "If a data set is perfectly symmetrical with no outliers, what is generally true about the mean and median?",
                "options": [
                    "The mean is always double the median",
                    "The mean and median are approximately equal",
                    "The median is always negative",
                    "The mean cannot be calculated"
                ],
                "correct": 1,
                "explanation": "In symmetric distributions, the balance point (mean) coincides with the middle point (median)."
            }
        ]
    },

    # Slide 10
    {
        "slide_num": 10,
        "badge": "Section 5.2",
        "section": "Representative Values",
        "title": "Of Ends and the Essence: Heights & Variations",
        "sim_id": "sim-height-distribution",
        "narration": "In 'Of Ends and the Essence', students measure everyone's height in class. Are students clustered around a common height, or are they spread all over? Let us examine classroom distributions!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-teal-500/10 border border-teal-500/30 rounded-xl">
    <h4 class="font-bold text-teal-300 text-sm mb-1">📏 The Classroom Height Survey</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      Suppose a Class 7 section of $20$ students measures their heights to the nearest centimeter. We observe both the <b>ends</b> (minimum and maximum boundaries) and the <b>essence</b> (the central clustering tendency).
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-rose-300 mb-1">1. The Ends (Boundaries)</div>
      <p class="text-slate-300">
        • Shortest student: $132\text{ cm}$<br>
        • Tallest student: $158\text{ cm}$<br>
        • Range: $158 - 132 = \mathbf{26\text{ cm}}$
      </p>
      <p class="mt-2 text-slate-400">Establishes the boundary span of the class.</p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-amber-300 mb-1">2. The Middle (Median)</div>
      <p class="text-slate-300">
        Sorting all $20$ heights, the 10th and 11th values are both $144\text{ cm}$.<br>
        $\text{Median} = \mathbf{144\text{ cm}}$.
      </p>
      <p class="mt-2 text-slate-400">Half the class is $\le 144\text{ cm}$; half is $\ge 144\text{ cm}$.</p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-emerald-300 mb-1">3. The Essence (Mean)</div>
      <p class="text-slate-300">
        Sum of all 20 heights = $2890\text{ cm}$.<br>
        $\text{Mean} = \frac{2890}{20} = \mathbf{144.5\text{ cm}}$.
      </p>
      <p class="mt-2 text-slate-400">The mean and median are closely aligned, showing symmetric clustering.</p>
    </div>
  </div>

  <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-indigo-300">Practical Application:</span> School uniform makers use these representative values to determine standard sizes (S, M, L) so that uniforms fit the greatest number of students without bespoke tailoring.
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "If the shortest student in class is 128 cm and the tallest is 162 cm, what is the range of student heights?",
                "options": ["24 cm", "30 cm", "34 cm", "40 cm"],
                "correct": 2,
                "explanation": "Range = Maximum - Minimum = 162 - 128 = 34 cm."
            },
            {
                "question": "Why do the mean and median height of 20 typical students in a classroom usually turn out very close to each other?",
                "options": [
                    "Because all heights in human populations are naturally identical",
                    "Because natural biological traits like height follow symmetric, bell-shaped distributions with no extreme million-centimeter outliers",
                    "Because students refuse to be measured",
                    "Because math rules force them to be identical"
                ],
                "correct": 1,
                "explanation": "Human heights are normally and symmetrically distributed without wild outliers, causing mean and median to closely coincide."
            }
        ]
    },

    # Slide 11
    {
        "slide_num": 11,
        "badge": "Section 5.2",
        "section": "Representative Values",
        "title": "Time Estimation Experiments",
        "sim_id": "sim-time-estimator",
        "narration": "Close your eyes! Without looking at a clock, raise your hand when you think exactly 30 seconds have passed. When a whole class does this, we discover the fascinating psychology of human time estimation!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-amber-500/10 border border-amber-500/30 rounded-xl">
    <h4 class="font-bold text-amber-300 text-sm mb-1">⏱️ The 30-Second Perception Experiment</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      In Section 5.2, NCERT invites students to conduct a live experiment: estimate a 30-second interval in silence. A teacher records the actual stopwatch time when each student raises their hand.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-cyan-300 mb-1">Sample Classroom Results ($n = 25$)</div>
      <p class="text-slate-300">Estimates ranged from $19\text{ seconds}$ to $44\text{ seconds}$:</p>
      <ul class="mt-2 space-y-1 text-slate-300">
        <li>• Minimum estimate: $19\text{ s}$ (counted too fast)</li>
        <li>• Maximum estimate: $44\text{ s}$ (counted too slow)</li>
        <li>• Median estimate: $\mathbf{28\text{ s}}$</li>
        <li>• Mean estimate: $\mathbf{28.4\text{ s}}$</li>
      </ul>
      <p class="mt-2 text-slate-400">Notice that humans tend to slightly underestimate time when sitting quietly waiting!</p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-emerald-300 mb-1">Statistical Lessons from Measurement</div>
      <ul class="space-y-1.5 text-slate-300 list-disc list-inside">
        <li><b>Measurement Error:</b> Every human measurement carries natural variability.</li>
        <li><b>The Wisdom of the Crowd:</b> Individual estimates were off by up to $14\text{ seconds}$, yet the class average ($28.4\text{ s}$) was remarkably close to the true $30\text{ seconds}$!</li>
        <li>Averaging multiple independent measurements cancels out random positive and negative errors.</li>
      </ul>
    </div>
  </div>

  <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-indigo-300">Scientific Foundation:</span> This is why astronomers and physicists take $10$ or $100$ repeated measurements and compute the mean to determine physical constants accurately.
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "In a time estimation test, four students guessed 24s, 28s, 32s, and 36s. What was the average estimate?",
                "options": ["28s", "30s", "31s", "32s"],
                "correct": 1,
                "explanation": "Sum = 24 + 28 + 32 + 36 = 120s. Mean = 120 / 4 = 30 seconds."
            },
            {
                "question": "Why do scientists repeat experiments multiple times and take the average of the results?",
                "options": [
                    "To waste laboratory chemicals",
                    "Because random errors in individual trials balance out, giving a more reliable estimate",
                    "Because single trials are illegal in science",
                    "To ensure the result is always zero"
                ],
                "correct": 1,
                "explanation": "Averaging repeated trials mitigates random experimental fluctuations and increases measurement precision."
            }
        ]
    },

    # Slide 12
    {
        "slide_num": 12,
        "badge": "Section 5.3",
        "section": "Visualising Data",
        "title": "From Single to Clustered Column Graphs",
        "sim_id": "sim-graph-type-selector",
        "narration": "A single bar graph displays one piece of information per category. But what if we want to compare girls and boys, or 2020 vs 2025? Enter Clustered Column Graphs, also known as Double Bar Graphs!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-purple-500/10 border border-purple-500/30 rounded-xl">
    <h4 class="font-bold text-purple-300 text-sm mb-1">📊 The Evolution of Bar Graphs</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      A <b>single bar graph</b> displays one numerical value for each category along an axis. But real-world data often demands comparing two distinct groups side-by-side across the same categories.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-cyan-300 mb-1">Single Bar Graph (1 Variable)</div>
      <p class="text-slate-300">
        Example: Total books sold by subject (Math: 40, Science: 50, English: 30).
      </p>
      <p class="text-slate-400 mt-2">
        • Single bar for each category.<br>
        • Cannot show how Grade 6 vs Grade 7 students contributed separately.
      </p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-amber-500/40">
      <div class="font-bold text-amber-300 mb-1">Clustered Column Graph (Double Bar)</div>
      <p class="text-slate-300">
        Example: Comparing Book Sales in Term 1 vs Term 2 side-by-side!
      </p>
      <p class="text-slate-400 mt-2">
        • Two adjoining bars for each category.<br>
        • Distinct colors or patterns differentiate the two series.<br>
        • A <b>legend (key)</b> clearly identifies which color represents which group.
      </p>
    </div>
  </div>

  <div class="p-3 bg-teal-500/10 border border-teal-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-teal-300">Essential Rule:</span> The width of every bar and the gap between clusters must remain strictly uniform across the entire graph. Only the heights of bars encode data values!
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the primary advantage of a clustered column graph (double bar graph) over a single bar graph?",
                "options": [
                    "It takes up less printer ink",
                    "It allows direct side-by-side comparison of two related datasets across the same categories",
                    "It makes all numbers look larger",
                    "It eliminates the need for an axis scale"
                ],
                "correct": 1,
                "explanation": "Double bar graphs place two data series adjacent to each other for effortless comparison across categories."
            },
            {
                "question": "What is the purpose of the 'Key' or 'Legend' in a double bar graph?",
                "options": [
                    "To unlock a secret mathematical door",
                    "To identify which color or shading corresponds to which data group",
                    "To show who drew the graph",
                    "To give the title of the school"
                ],
                "correct": 1,
                "explanation": "The key or legend defines what each colored bar represents (e.g., Blue = Town A, Amber = Town B)."
            }
        ]
    },

    # Slide 13
    {
        "slide_num": 13,
        "badge": "Section 5.3",
        "section": "Visualising Data",
        "title": "Anatomy of a Double Bar Graph",
        "sim_id": "sim-double-bar-builder",
        "narration": "Let us build a double bar graph step-by-step. We choose a sensible scale on the vertical axis, label our categories, and compare performance between Quarter 1 and Quarter 2!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-blue-500/10 border border-blue-500/30 rounded-xl">
    <h4 class="font-bold text-blue-300 text-sm mb-1">🛠️ Structural Elements of Clustered Graphs</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      Constructing an accurate double bar graph requires four foundational elements executed with geometric precision.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-amber-300 mb-1">1. Choosing the Scale (Vertical Axis)</div>
      <p class="text-slate-300 leading-relaxed">
        The scale must comfortably accommodate the maximum value without wasting canvas space.
      </p>
      <div class="p-2 my-1.5 bg-slate-900/60 rounded font-mono text-cyan-200">
        If max value is 65: Scale = 1 cm : 10 units (0, 10, 20 ... 70).<br>
        If max value is 600: Scale = 1 cm : 100 units.
      </div>
      <p class="text-slate-400">Start the vertical axis at zero ($0$) to avoid visual distortion!</p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-emerald-300 mb-1">2. Horizontal Layout & Clustering</div>
      <ul class="space-y-1.5 text-slate-300 list-disc list-inside">
        <li>Categories are marked along the horizontal axis with equal spacing.</li>
        <li>Within each category, the two bars touch or sit immediately adjacent without gap.</li>
        <li>A distinct gap separates one category cluster from the next cluster.</li>
        <li>Color order must be consistent (e.g., Blue always first, Amber always second).</li>
      </ul>
    </div>
  </div>

  <div class="p-3 bg-slate-900/60 rounded-xl border border-slate-700/50 text-xs text-slate-300">
    <b>Self-Check Rule:</b> Can someone who has never seen your raw data table answer "Which town scored higher in April?" in under $2$ seconds by glancing at your graph? If yes, your graph is successful!
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "If the highest recorded value in a data table is 88 marks, which scale on the vertical axis is most appropriate for a graph sheet with 10 cm height?",
                "options": [
                    "1 unit per cm",
                    "10 units per cm (so 0 to 100 cm occupies 10 cm)",
                    "100 units per cm",
                    "500 units per cm"
                ],
                "correct": 1,
                "explanation": "A scale of 10 units per cm easily fits 88 marks (reaching 8.8 cm height) with comfortable headroom up to 100."
            },
            {
                "question": "Why is it considered bad practice to start the vertical frequency axis at 50 instead of 0 without a break symbol (kink)?",
                "options": [
                    "It makes the page look untidy",
                    "It visually exaggerates tiny differences between bars, misleading the viewer",
                    "Numbers below 50 are unlucky",
                    "Pencils cannot draw numbers below 50"
                ],
                "correct": 1,
                "explanation": "Trunking the baseline without clear indication visually multiplies height differences, making a 5% difference look like a 500% difference."
            }
        ]
    },

    # Slide 14
    {
        "slide_num": 14,
        "badge": "Section 5.3",
        "section": "Visualising Data",
        "title": "Multi-Step Graphical Analysis",
        "sim_id": "sim-multistep-extractor",
        "narration": "True data mastery goes beyond just reading single bar heights. We compute totals, compare growth rates, and extract hidden conclusions from clustered graphs!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-teal-500/10 border border-teal-500/30 rounded-xl">
    <h4 class="font-bold text-teal-300 text-sm mb-1">🔍 Extracting Multi-Step Insights</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      A clustered column graph answers complex relational questions through a 3-tier analytical hierarchy:
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-cyan-300 mb-1">Tier 1: Direct Reading</div>
      <p class="text-slate-300">
        "What was the mango harvest in 2023?"<br>
        <i>Action:</i> Look up the bar height directly against the vertical scale.
      </p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-amber-300 mb-1">Tier 2: Difference & Gap</div>
      <p class="text-slate-300">
        "In which fruit was the production increase largest from 2023 to 2024?"<br>
        <i>Action:</i> Compute $\text{Bar}_2 - \text{Bar}_1$ across all fruit clusters and find the maximum gap.
      </p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-purple-300 mb-1">Tier 3: Aggregation</div>
      <p class="text-slate-300">
        "What was the total combined production of all fruits over both years?"<br>
        <i>Action:</i> Sum all bars together across both series.
      </p>
    </div>
  </div>

  <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl text-xs text-slate-300">
    <b>Sample Comparison:</b> In mathematics marks, Amit improved from $60$ (Term 1) to $85$ (Term 2) (gain of $+25$). In English, he moved from $70$ to $75$ (gain of $+5$). The graph instantly shows math had the steepest growth trajectory!
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "In a double bar graph of school sports, 45 boys and 55 girls play badminton, while 60 boys and 20 girls play cricket. In which sport is the participation gap between boys and girls largest?",
                "options": [
                    "Badminton (gap = 10)",
                    "Cricket (gap = 40)",
                    "Both have identical gaps",
                    "Neither sport has players"
                ],
                "correct": 1,
                "explanation": "In cricket, the difference between boys and girls is 60 - 20 = 40, which is significantly larger than the badminton gap of 55 - 45 = 10."
            },
            {
                "question": "How do you calculate the total annual attendance of both grades in August from a double bar graph showing Grade 7 = 92 and Grade 8 = 88?",
                "options": [
                    "92 - 88 = 4",
                    "92 + 88 = 180",
                    "92 × 88 = 8096",
                    "(92 + 88) / 2 = 90"
                ],
                "correct": 1,
                "explanation": "Total combined attendance is found by summing the heights of both grade bars: 92 + 88 = 180."
            }
        ]
    },

    # Slide 15
    {
        "slide_num": 15,
        "badge": "Section 5.4",
        "section": "Data Detective",
        "title": "Data Detective: Trends Over Time",
        "sim_id": "sim-growth-trends-tracker",
        "narration": "Welcome to Section 5.4: The Data Detective! In 1920, a 12-year-old child had an average height of 135 cm. Today, it is over 148 cm! How do nutrition and public health shape data across decades?",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-emerald-500/10 border border-emerald-500/30 rounded-xl">
    <h4 class="font-bold text-emerald-300 text-sm mb-1">🕵️ Trends: Spotting the Story in Data</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      A <b>trend</b> is a long-term general movement or direction in a dataset over time. As a Data Detective, your job is not just to compute arithmetic, but to ask: <i>"What story is this data telling us about the world?"</i>
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-cyan-300 mb-1">Case Study: Child Growth Over a Century</div>
      <p class="text-slate-300 leading-relaxed">
        Surveys tracking 12-year-old school children across decades reveal a fascinating upward trend:
      </p>
      <ul class="my-1.5 space-y-1 font-mono text-amber-200">
        <li>• Year 1920: Average Height = $135\text{ cm}$</li>
        <li>• Year 1960: Average Height = $141\text{ cm}$</li>
        <li>• Year 2000: Average Height = $147\text{ cm}$</li>
        <li>• Year 2025: Average Height = $150\text{ cm}$</li>
      </ul>
      <p class="text-slate-400">Total increase of $+15\text{ cm}$ across a century!</p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-emerald-300 mb-1">The Detective's Explanation</div>
      <ul class="space-y-1.5 text-slate-300 list-disc list-inside">
        <li><b>Improved Nutrition:</b> Better access to protein, milk, and balanced diets.</li>
        <li><b>Medical Advances:</b> Eradication of childhood infectious diseases through vaccines.</li>
        <li><b>Clean Water & Sanitation:</b> Preventing chronic nutrient malabsorption.</li>
        <li><b>Secular Growth Trend:</b> Documented globally by the World Health Organization (WHO).</li>
      </ul>
    </div>
  </div>

  <div class="p-3 bg-purple-500/10 border border-purple-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-purple-300">Insight:</span> Numbers do not live in a vacuum. A graph of child heights over decades is actually a mirror of economic development and medical science!
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is meant by an 'Upward Trend' in a multi-decade time survey?",
                "options": [
                    "The graph paper was tilted upward",
                    "The values show a sustained general increase over sequential time periods",
                    "The measurements became invalid",
                    "All numbers reached infinity"
                ],
                "correct": 1,
                "explanation": "A trend describes a persistent directional shift in data over time."
            },
            {
                "question": "If average life expectancy in a country rose from 45 years in 1950 to 70 years in 2020, what conclusion can a data detective draw?",
                "options": [
                    "People in 1950 forgot how to count birthdays",
                    "Substantial improvements occurred in healthcare, sanitation, and living standards over the 70-year period",
                    "Clocks tick faster today than in 1950",
                    "The population shrank to zero"
                ],
                "correct": 1,
                "explanation": "Sustained positive shifts in health metrics reflect underlying socioeconomic and healthcare advancements."
            }
        ]
    },

    # Slide 16
    {
        "slide_num": 16,
        "badge": "Section 5.4",
        "section": "Data Detective",
        "title": "Patterns, Biases & Misleading Claims",
        "sim_id": "sim-misleading-graph-buster",
        "narration": "Numbers can tell the truth, but they can also be twisted to deceive! Let us train our statistical radar to detect truncated axes, cherry-picked samples, and correlation traps.",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-rose-500/10 border border-rose-500/30 rounded-xl">
    <h4 class="font-bold text-rose-300 text-sm mb-1">⚠️ How Data Can Be Misused</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      A savvy citizen must distinguish honest statistical reporting from manipulative graphics and false claims.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-amber-300 mb-1">1. The Truncated Y-Axis</div>
      <p class="text-slate-300">
        By zooming in on values between $98\%$ and $100\%$ without starting at $0$, a tiny $0.5\%$ difference is made to look like a mountain!
      </p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-rose-300 mb-1">2. Sample Selection Bias</div>
      <p class="text-slate-300">
        "9 out of 10 people prefer Brand X!"<br>
        <i>The catch:</i> They only surveyed 10 people standing inside the Brand X factory store!
      </p>
    </div>

    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-cyan-300 mb-1">3. Correlation vs Causation</div>
      <p class="text-slate-300">
        Ice cream sales and swimming pool drownings both rise in June. Does eating ice cream cause drowning? No! Both are caused by hot summer weather!
      </p>
    </div>
  </div>

  <div class="p-3 bg-emerald-500/10 border border-emerald-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-emerald-300">Prof. Mahalanobis's Legacy:</span> In 1931, Prasanta Chandra Mahalanobis founded the Indian Statistical Institute and introduced large-scale randomized sample surveys in India—proving that reliable sample design protects truth from bias!
  </div>
</div>
""",
        "checkpoints": [
            {
                "question": "A toothpaste company claims '80% of dentists recommend our paste'. If they only interviewed 5 selected dentists on their payroll, what statistical error was committed?",
                "options": [
                    "Division by zero error",
                    "Sample selection bias and unrepresentative sample size",
                    "Using roman numerals",
                    "A geometry angle error"
                ],
                "correct": 1,
                "explanation": "A tiny, biased, and financially conflicted sample cannot be generalized to the entire dental profession."
            },
            {
                "question": "Why is 'Correlation does not imply Causation' a cornerstone rule of statistics?",
                "options": [
                    "Because correlation only exists in algebra",
                    "Because two events may rise together due to a third hidden factor (confounder) without one causing the other",
                    "Because scientists hate graphs",
                    "Because causes only happen on Tuesdays"
                ],
                "correct": 1,
                "explanation": "Co-occurring patterns do not prove direct cause-and-effect; common underlying variables often drive both."
            }
        ]
    },

    # Slide 17: Quiz Challenge 1
    {
        "slide_num": 17,
        "badge": "Mastery Quiz 1",
        "section": "Section 5.1 & 5.2",
        "title": "Mastery Challenge: Questions, Statements & The Mean",
        "quiz_range": [1, 10],
        "is_quiz": True,
        "narration": "Test your mastery on Statistical Questions, Statements, and the Arithmetic Mean! Complete all 10 questions to prove your analytical foundation."
    },

    # Slide 18: Quiz Challenge 2
    {
        "slide_num": 18,
        "badge": "Mastery Quiz 2",
        "section": "Section 5.2",
        "title": "Mastery Challenge: Onion Prices, Dot Plots & Medians",
        "quiz_range": [11, 20],
        "is_quiz": True,
        "narration": "Challenge round two! Put your knowledge of price variations, dot plots, outliers, and the median to the test."
    },

    # Slide 19: Quiz Challenge 3
    {
        "slide_num": 19,
        "badge": "Mastery Quiz 3",
        "section": "Section 5.3",
        "title": "Mastery Challenge: Clustered Columns & Double Bars",
        "quiz_range": [21, 30],
        "is_quiz": True,
        "narration": "Round three! Inspect double bar graphs, verify scales, compute cross-category differences, and decode clustered visualizations."
    },

    # Slide 20: Quiz Challenge 4
    {
        "slide_num": 20,
        "badge": "Mastery Quiz 4",
        "section": "Section 5.4 & Summary",
        "title": "Mastery Challenge: The Data Detective & Grand Finale",
        "quiz_range": [31, 40],
        "is_quiz": True,
        "narration": "Final round! Act as the ultimate Data Detective: spot secular trends, catch misleading axes, analyze distributions, and complete the chapter."
    }
]

# 40 Quiz Questions with Detailed Step-by-Step Pop-up Solutions
QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "Which of the following questions is a statistical question?",
        "options": [
            "How many states are in India?",
            "What is the boiling point of water at sea level?",
            "How many minutes does it take students in your class to travel to school?",
            "Who was the first President of India?"
        ],
        "correct": 2,
        "solution": r"""
$$\textbf{Identifying Statistical Questions:}$$
1. A statistical question must anticipate **variability** in the responses collected.
2. The number of states (28), the boiling point of water ($100^\circ\text{C}$), and the first President (Dr. Rajendra Prasad) are all single deterministic facts with zero variability.
3. In contrast, commute times vary across students ($5\text{ min}$, $15\text{ min}$, $40\text{ min}$, etc.), requiring data collection and statistical analysis.
$$\text{Correct Choice: Option C}$$
"""
    },
    # Q2
    {
        "id": 2,
        "question": "Five friends have 6, 8, 10, 12, and 14 pencils. If they pool them together and distribute them equally, how many does each receive?",
        "options": ["8 pencils", "10 pencils", "12 pencils", "14 pencils"],
        "correct": 1,
        "solution": r"""
$$\textbf{Fair-Share (Samamiti) Calculation:}$$
1. Calculate the total pooled quantity:
   $$\text{Total} = 6 + 8 + 10 + 12 + 14 = 50\text{ pencils}$$
2. Divide the total equally among the $5$ friends:
   $$\text{Equal Share} = \frac{50}{5} = \mathbf{10\text{ pencils}}$$
3. This equalized share is precisely the Arithmetic Mean.
"""
    },
    # Q3
    {
        "id": 3,
        "question": "What is the arithmetic mean of 15, 20, 25, 30, and 35?",
        "options": ["20", "25", "27.5", "30"],
        "correct": 1,
        "solution": r"""
$$\textbf{Computing the Arithmetic Mean:}$$
1. Sum of observations:
   $$\sum x_i = 15 + 20 + 25 + 30 + 35 = 125$$
2. Number of observations: $n = 5$.
3. Mean formula:
   $$\text{Mean} = \frac{125}{5} = \mathbf{25}$$
Notice that for an evenly spaced sequence, the mean is the middle term.
"""
    },
    # Q4
    {
        "id": 4,
        "question": "The mean of four numbers is 18. What is their total sum?",
        "options": ["54", "72", "90", "36"],
        "correct": 1,
        "solution": r"""
$$\textbf{Inverse Mean Computation:}$$
1. The mean is defined as:
   $$\text{Mean} = \frac{\text{Sum}}{n}$$
2. Rearranging to find the sum:
   $$\text{Sum} = \text{Mean} \times n = 18 \times 4 = \mathbf{72}$$
"""
    },
    # Q5
    {
        "id": 5,
        "question": "A student scored 75, 80, 85, and 90 in four tests. What score does she need on the 5th test to have an overall mean of 85?",
        "options": ["85", "90", "95", "100"],
        "correct": 2,
        "solution": r"""
$$\textbf{Target Mean Analysis:}$$
1. Required total for 5 tests with mean $85$:
   $$\text{Target Sum} = 5 \times 85 = 425$$
2. Sum of the first four tests:
   $$\text{Current Sum} = 75 + 80 + 85 + 90 = 330$$
3. Required 5th score:
   $$\text{Score} = 425 - 330 = \mathbf{95}$$
"""
    },
    # Q6
    {
        "id": 6,
        "question": "Which of the following statements is a statistical claim?",
        "options": [
            "A triangle has 3 sides.",
            "Water expands when it freezes.",
            "68% of Class 7 students participate in extra-curricular activities.",
            "Iron is a chemical element."
        ],
        "correct": 2,
        "solution": r"""
$$\textbf{Identifying Statistical Claims:}$$
1. A statistical claim reports aggregate proportions, numerical frequencies, or empirical survey data across a group.
2. 68% summarizes an empirical survey of student participation.
3. The other choices are geometric definitions or scientific universal laws.
"""
    },
    # Q7
    {
        "id": 7,
        "question": "What is the mean of the first five natural numbers (1, 2, 3, 4, 5)?",
        "options": ["2.5", "3.0", "3.5", "15"],
        "correct": 1,
        "solution": r"""
$$\textbf{Mean of First 5 Natural Numbers:}$$
1. Observations: $1, 2, 3, 4, 5$.
2. Sum: $1 + 2 + 3 + 4 + 5 = 15$.
3. Count: $n = 5$.
$$\text{Mean} = \frac{15}{5} = \mathbf{3}$$
"""
    },
    # Q8
    {
        "id": 8,
        "question": "If a dataset consists of [10, 10, 10, 10, 10], what is its arithmetic mean?",
        "options": ["0", "5", "10", "50"],
        "correct": 2,
        "solution": r"""
$$\textbf{Mean of Identical Values:}$$
1. $\text{Sum} = 10 \times 5 = 50$.
2. $\text{Mean} = \frac{50}{5} = \mathbf{10}$.
When all values in a group are identical, their mean is that constant value itself.
"""
    },
    # Q9
    {
        "id": 9,
        "question": "The ages of five family members are 10, 12, 14, 40, and 44. What is the mean age?",
        "options": ["20 years", "24 years", "26 years", "30 years"],
        "correct": 1,
        "solution": r"""
$$\textbf{Calculating Mean Family Age:}$$
1. Sum $= 10 + 12 + 14 + 40 + 44 = 120\text{ years}$.
2. Number of members $= 5$.
3. Mean $= \frac{120}{5} = \mathbf{24\text{ years}}$.
"""
    },
    # Q10
    {
        "id": 10,
        "question": "In ancient Indian mathematics, what was the term 'Samamiti' used to convey?",
        "options": [
            "Calculating circle circumferences",
            "An equalized or leveling measure of distributed quantities",
            "Dividing fractions by reciprocals",
            "Counting solar eclipses"
        ],
        "correct": 1,
        "solution": r"""
$$\textbf{Historical Indian Concept: Samamiti:}$$
1. *Sama* means equal/balanced; *miti* means measure.
2. *Samamiti* represents an equalized, balanced measure obtained by leveling out uneven shares, directly corresponding to the modern Arithmetic Mean.
"""
    },

    # Q11
    {
        "id": 11,
        "question": "The recorded onion prices in Town B over 5 months were ₹15, ₹25, ₹10, ₹50, and ₹35. What is the Range of onion prices?",
        "options": ["₹35", "₹40", "₹45", "₹50"],
        "correct": 1,
        "solution": r"""
$$\textbf{Range Calculation:}$$
1. Maximum price $= \text{Rs. } 50$.
2. Minimum price $= \text{Rs. } 10$.
3. Formula for Range:
   $$\text{Range} = \text{Maximum} - \text{Minimum} = 50 - 10 = \mathbf{\text{Rs. } 40}$$
"""
    },
    # Q12
    {
        "id": 12,
        "question": "In a dot plot, what does a vertical stack of 4 dots above number 15 indicate?",
        "options": [
            "15 has been multiplied by 4",
            "The value 15 occurred exactly 4 times in the dataset",
            "The number 15 is an outlier",
            "The mean is 60"
        ],
        "correct": 1,
        "explanation": "Each dot in a dot plot represents one occurrence of that data value. A stack of 4 dots means frequency = 4."
    },
    # Q13
    {
        "id": 13,
        "question": "Consider the dataset: 3, 5, 7, 9, 11. What is the Median?",
        "options": ["5", "7", "9", "35"],
        "correct": 1,
        "solution": r"""
$$\textbf{Finding the Median (Odd Count):}$$
1. The numbers are already sorted in ascending order: $3, 5, \mathbf{7}, 9, 11$.
2. Total items $n = 5$ (odd).
3. The middle position is $\frac{5+1}{2} = 3\text{rd}$ item.
$$\text{Median} = \mathbf{7}$$
"""
    },
    # Q14
    {
        "id": 14,
        "question": "Find the median of the following numbers: 14, 8, 22, 16, 5, 19, 11.",
        "options": ["11", "14", "16", "19"],
        "correct": 1,
        "solution": r"""
$$\textbf{Median with Sorting Step:}$$
1. **Crucial First Step: Sort ascending:**
   $$5, 8, 11, \mathbf{14}, 16, 19, 22$$
2. Total count $n = 7$.
3. The 4th item sits in the exact middle:
   $$\text{Median} = \mathbf{14}$$
"""
    },
    # Q15
    {
        "id": 15,
        "question": "Find the median of the even-numbered dataset: 12, 18, 6, 24, 14, 10.",
        "options": ["12", "13", "14", "16"],
        "correct": 1,
        "solution": r"""
$$\textbf{Median of an Even Dataset:}$$
1. **Sort ascending:**
   $$6, 10, \mathbf{12, 14}, 18, 24$$
2. Count $n = 6$ (even). The middle two items are the 3rd ($12$) and 4th ($14$).
3. Take their arithmetic mean:
   $$\text{Median} = \frac{12 + 14}{2} = \frac{26}{2} = \mathbf{13}$$
"""
    },
    # Q16
    {
        "id": 16,
        "question": "Consider the salaries: ₹12,000, ₹14,000, ₹13,000, ₹15,000, and ₹3,50,000. Which measure of central tendency gives the most realistic picture of a typical employee's income?",
        "options": [
            "Arithmetic Mean (₹80,800)",
            "Median (₹14,000)",
            "Maximum (₹3,50,000)",
            "Total Sum"
        ],
        "correct": 1,
        "solution": r"""
$$\textbf{Choosing Central Tendency in Skewed Data:}$$
1. Sorting the salaries:
   $$12000, 13000, \mathbf{14000}, 15000, 350000$$
2. The extreme outlier of ₹3,50,000 pulls the mean up to:
   $$\text{Mean} = \frac{404000}{5} = \text{Rs. } 80,800$$
3. However, four out of five workers earn $\le \text{Rs. } 15,000$.
4. The **Median** ($\text{Rs. } 14,000$) is unaffected by the outlier and accurately represents typical worker income.
"""
    },
    # Q17
    {
        "id": 17,
        "question": "If you replace the largest number in a dataset of 9 items with a number 1,000 times larger, what happens to the Median?",
        "options": [
            "It increases by 1,000 times",
            "It decreases to zero",
            "It remains completely unchanged",
            "It becomes undefined"
        ],
        "correct": 2,
        "solution": r"""
$$\textbf{Robustness of the Median:}$$
1. In a sorted 9-item list, the median is the 5th item:
   $$x_1, x_2, x_3, x_4, \mathbf{x_5}, x_6, x_7, x_8, x_9$$
2. Changing the 9th item ($x_9$) to an astronomically huge number changes its magnitude, but it remains at rank position 9.
3. Position 5 is unaffected, so the Median remains strictly unchanged!
"""
    },
    # Q18
    {
        "id": 18,
        "question": "In a classroom height survey, 7 students measured 140, 142, 143, 144, 145, 146, 148 cm. What is the median height?",
        "options": ["143 cm", "144 cm", "145 cm", "146 cm"],
        "correct": 1,
        "solution": r"""
$$\textbf{Classroom Height Median:}$$
1. The 7 values are sorted:
   $$140, 142, 143, \mathbf{144}, 145, 146, 148$$
2. Middle item is the 4th item $= \mathbf{144\text{ cm}}$.
"""
    },
    # Q19
    {
        "id": 19,
        "question": "What is the Range of the heights: 135 cm, 142 cm, 158 cm, 138 cm, 150 cm?",
        "options": ["15 cm", "20 cm", "23 cm", "25 cm"],
        "correct": 2,
        "solution": r"""
$$\textbf{Range Calculation:}$$
1. Maximum height $= 158\text{ cm}$.
2. Minimum height $= 135\text{ cm}$.
$$\text{Range} = 158 - 135 = \mathbf{23\text{ cm}}$$
"""
    },
    # Q20
    {
        "id": 20,
        "question": "Which of the following is an outlier in the list: [22, 24, 21, 23, 25, 22, 98]?",
        "options": ["21", "22", "25", "98"],
        "correct": 3,
        "explanation": "98 is isolated and drastically distant from the main cluster of values clustered tightly around 21-25."
    },

    # Q21
    {
        "id": 21,
        "question": "In a double bar graph comparing rainfall in two cities, what does each pair of clustered bars represent?",
        "options": [
            "Rainfall in two different decades",
            "Rainfall for City A and City B during the same month or category",
            "The sum of all rain in the country",
            "The temperature of the ocean"
        ],
        "correct": 1,
        "explanation": "Each cluster pairs the measurements of the two cities side-by-side for that specific category (e.g. July)."
    },
    # Q22
    {
        "id": 22,
        "question": "A bar graph has a vertical scale where 1 cm represents 25 students. How high will a bar be for a category with 150 students?",
        "options": ["4 cm", "5 cm", "6 cm", "8 cm"],
        "correct": 2,
        "solution": r"""
$$\textbf{Bar Height Scale Conversion:}$$
1. Given scale: $1\text{ cm} = 25\text{ students}$.
2. Number of students $= 150$.
$$\text{Bar Height} = \frac{150}{25} = \mathbf{6\text{ cm}}$$
"""
    },
    # Q23
    {
        "id": 23,
        "question": "In a double bar graph, the bars for English scores in Term 1 and Term 2 are 65 and 80. By how much did the score improve?",
        "options": ["10 marks", "15 marks", "20 marks", "25 marks"],
        "correct": 1,
        "solution": r"""
$$\textbf{Improvement Gap:}$$
$$\text{Improvement} = \text{Term 2} - \text{Term 1} = 80 - 65 = \mathbf{15\text{ marks}}$$
"""
    },
    # Q24
    {
        "id": 24,
        "question": "In a school library survey, Grade 7 borrowed 120 storybooks and 80 science books. Grade 8 borrowed 90 storybooks and 110 science books. What is the total number of science books borrowed by both grades?",
        "options": ["170", "190", "200", "210"],
        "correct": 1,
        "solution": r"""
$$\textbf{Aggregating Category Columns:}$$
1. Science books borrowed by Grade 7 $= 80$.
2. Science books borrowed by Grade 8 $= 110$.
$$\text{Total Science Books} = 80 + 110 = \mathbf{190}$$
"""
    },
    # Q25
    {
        "id": 25,
        "question": "Which of the following rules is MANDATORY when drawing a bar graph?",
        "options": [
            "All bars must be colored red",
            "The widths of all bars must be uniform and spaces between categories must be equal",
            "Bars must always be tilted at 45 degrees",
            "The graph must have at least 100 bars"
        ],
        "correct": 1,
        "explanation": "Uniform bar widths and equal inter-cluster spacing ensure that area is strictly proportional to height."
    },
    # Q26
    {
        "id": 26,
        "question": "In a double bar graph comparing girls and boys in five clubs, in Art Club: Girls = 45, Boys = 15. In Sports Club: Girls = 30, Boys = 50. What is the difference in total membership between Sports Club and Art Club?",
        "options": ["10 members", "20 members", "30 members", "0 members"],
        "correct": 1,
        "solution": r"""
$$\textbf{Multi-Step Cluster Comparison:}$$
1. Total Art Club membership $= 45 + 15 = 60\text{ members}$.
2. Total Sports Club membership $= 30 + 50 = 80\text{ members}$.
3. Difference $= 80 - 60 = \mathbf{20\text{ members}}$.
"""
    },
    # Q27
    {
        "id": 27,
        "question": "Why is a broken scale (zigzag kink line '〰️') used near the origin of an axis in some graphs?",
        "options": [
            "To indicate the graph was torn by accident",
            "To indicate that the scale from 0 to a large starting number is collapsed to save space without distorting relative bar differences",
            "To show negative numbers",
            "To make the drawing artistic"
        ],
        "correct": 1,
        "explanation": "A kink indicates an intentional omission of empty range between 0 and the first data value, alerting the reader."
    },
    # Q28
    {
        "id": 28,
        "question": "In a quarterly sales double bar graph, Town A sold [40, 50, 60, 50] cycles and Town B sold [30, 45, 70, 55] cycles. Which town sold more cycles overall across the year?",
        "options": [
            "Town A (200 cycles)",
            "Town B (200 cycles)",
            "Both sold the exact same total (200 cycles)",
            "Town A sold 250 cycles"
        ],
        "correct": 2,
        "solution": r"""
$$\textbf{Comparing Annual Totals:}$$
1. Town A Total:
   $$40 + 50 + 60 + 50 = \mathbf{200\text{ cycles}}$$
2. Town B Total:
   $$30 + 45 + 70 + 55 = \mathbf{200\text{ cycles}}$$
Both towns achieved the exact same annual sales of 200 cycles.
"""
    },
    # Q29
    {
        "id": 29,
        "question": "From the same data as Q28 (Town A: 40, 50, 60, 50 vs Town B: 30, 45, 70, 55), in which Quarter did Town B outperform Town A by the largest margin?",
        "options": ["Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"],
        "correct": 2,
        "solution": r"""
$$\textbf{Quarterly Margins for Town B:}$$
- Q1: $30 - 40 = -10$ (Town A was ahead)
- Q2: $45 - 50 = -5$ (Town A was ahead)
- Q3: $70 - 60 = \mathbf{+10}$ (Town B ahead by 10)
- Q4: $55 - 50 = +5$ (Town B ahead by 5)
Town B had its largest winning margin in Quarter 3 (+10 cycles).
"""
    },
    # Q30
    {
        "id": 30,
        "question": "If a bar of height 8 cm represents 160 trees, how many trees does each 1 cm on the axis represent?",
        "options": ["10 trees", "15 trees", "20 trees", "25 trees"],
        "correct": 2,
        "solution": r"""
$$\textbf{Determining Scale Unit:}$$
$$\text{Scale per cm} = \frac{160\text{ trees}}{8\text{ cm}} = \mathbf{20\text{ trees/cm}}$$
"""
    },

    # Q31
    {
        "id": 31,
        "question": "A historical survey found that 14-year-old boys in a region had an average height of 142 cm in 1950 and 156 cm in 2020. What is the average decadal growth rate over these 70 years (7 decades)?",
        "options": ["1 cm/decade", "2 cm/decade", "3 cm/decade", "14 cm/decade"],
        "correct": 1,
        "solution": r"""
$$\textbf{Decadal Trend Rate:}$$
1. Total height increase $= 156 - 142 = 14\text{ cm}$.
2. Number of decades $= \frac{2020 - 1950}{10} = 7\text{ decades}$.
3. Average growth per decade:
   $$\text{Rate} = \frac{14\text{ cm}}{7\text{ decades}} = \mathbf{2\text{ cm/decade}}$$
"""
    },
    # Q32
    {
        "id": 32,
        "question": "What is the primary danger of a 'Truncated Axis' graph where the vertical scale starts at 95% instead of 0%?",
        "options": [
            "It turns lines upside down",
            "It visually exaggerates tiny differences, misleading viewers into thinking small variations are massive",
            "It deletes half the data",
            "It changes all percentages to fractions"
        ],
        "correct": 1,
        "explanation": "Truncating the vertical axis magnifies minuscule differences, deceiving the casual reader."
    },
    # Q33
    {
        "id": 33,
        "question": "If two variables A and B show a strong positive correlation (when A rises, B also rises), what does this prove?",
        "options": [
            "A definitely causes B",
            "B definitely causes A",
            "There is an association between A and B, but it does NOT prove causation",
            "One of the measurements is fake"
        ],
        "correct": 2,
        "explanation": "Correlation proves mutual co-movement, not cause-and-effect. A confounding third factor may drive both."
    },
    # Q34
    {
        "id": 34,
        "question": "Who is celebrated as the Father of Modern Statistics in India and founder of the Indian Statistical Institute (ISI)?",
        "options": [
            "Aryabhata",
            "Bhaskaracharya",
            "Prof. Prasanta Chandra Mahalanobis",
            "Srinivasa Ramanujan"
        ],
        "correct": 2,
        "explanation": "Prof. P. C. Mahalanobis pioneered large-scale sample survey methodologies and founded ISI in Kolkata in 1931."
    },
    # Q35
    {
        "id": 35,
        "question": "In a dataset of test scores [10, 15, 18, 20, 22, 25, 30], what is the Median score?",
        "options": ["18", "20", "22", "25"],
        "correct": 1,
        "solution": r"""
$$\textbf{Locating the Median:}$$
1. Already sorted: $10, 15, 18, \mathbf{20}, 22, 25, 30$.
2. Total count $n = 7$ (odd).
3. The 4th item is the median $= \mathbf{20}$.
"""
    },
    # Q36
    {
        "id": 36,
        "question": "What is the Arithmetic Mean of the dataset: [10, 15, 18, 20, 22, 25, 30]?",
        "options": ["18", "20", "22", "24"],
        "correct": 1,
        "solution": r"""
$$\textbf{Calculating the Arithmetic Mean:}$$
1. $\text{Sum} = 10 + 15 + 18 + 20 + 22 + 25 + 30 = 140$.
2. Count $n = 7$.
$$\text{Mean} = \frac{140}{7} = \mathbf{20}$$
Notice in this symmetric dataset, Mean = Median = 20!
"""
    },
    # Q37
    {
        "id": 37,
        "question": "A researcher surveys 5 students in an elite chess club and announces: 'All Indian teenagers spend 4 hours daily playing chess!' What flaw is present here?",
        "options": [
            "Arithmetic calculation error",
            "Severe selection bias and unrepresentative sample size",
            "Using chess instead of cricket",
            "Measurement unit error"
        ],
        "correct": 1,
        "explanation": "Chess club members are not representative of all teenagers; generalizing from 5 club members is extreme selection bias."
    },
    # Q38
    {
        "id": 38,
        "question": "A set of 6 numbers has a sum of 150. If one number is removed, the mean of the remaining 5 numbers becomes 24. What was the value of the removed number?",
        "options": ["24", "26", "30", "36"],
        "correct": 2,
        "solution": r"""
$$\textbf{Finding the Removed Number:}$$
1. Original total sum of 6 numbers $= 150$.
2. The remaining 5 numbers have mean $24$:
   $$\text{New Sum} = 5 \times 24 = 120$$
3. The removed number must be the difference:
   $$\text{Removed Number} = 150 - 120 = \mathbf{30}$$
"""
    },
    # Q39
    {
        "id": 39,
        "question": "A shopkeeper sells 10 shirts on Monday, 12 on Tuesday, 14 on Wednesday, and 16 on Thursday. How many must he sell on Friday to have a 5-day daily mean of 15 shirts?",
        "options": ["18 shirts", "20 shirts", "23 shirts", "25 shirts"],
        "correct": 2,
        "solution": r"""
$$\textbf{Sales Target Calculation:}$$
1. Desired 5-day total $= 5 \times 15 = 75\text{ shirts}$.
2. Current 4-day sales $= 10 + 12 + 14 + 16 = 52\text{ shirts}$.
3. Required Friday sales:
   $$\text{Friday Sales} = 75 - 52 = \mathbf{23\text{ shirts}}$$
"""
    },
    # Q40
    {
        "id": 40,
        "question": "Which of the following summaries accurately distinguishes Mean and Median?",
        "options": [
            "Mean is the middle value; Median is the sum divided by count",
            "Mean incorporates every observation but is sensitive to outliers; Median is the sorted positional middle and is robust against outliers",
            "Mean only works for geometry; Median only works for currency",
            "Mean is always larger than Median in all possible datasets"
        ],
        "correct": 1,
        "solution": r"""
$$\textbf{The Core Definitional Distinction:}$$
1. **Arithmetic Mean:** Equal-share center of gravity ($\frac{\sum x}{n}$); takes all values into account, but easily hijacked by extreme outliers.
2. **Median:** Rank-order physical midpoint (50th percentile); ignores extreme magnitudes at the ends and remains stable.
$$\text{Correct Choice: Option B}$$
"""
    }
]

# Write to .agents/class7_math_connecting_the_dots_data.py
output_path = ".agents/class7_math_connecting_the_dots_data.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("# Generated data for NCERT Class 7 Mathematics - Chapter 5: Connecting the Dots...\n\n")
    f.write(f"SLIDES_DATA = {repr(SLIDES_DATA)}\n\n")
    f.write(f"QUIZ_QUESTIONS = {repr(QUIZ_QUESTIONS)}\n")

print(f"Generated {output_path} successfully!")
print(f"Total slides: {len(SLIDES_DATA)}, Total quiz questions: {len(QUIZ_QUESTIONS)}")

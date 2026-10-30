import json

def generate_data():
    CHAPTER_META = {
        "chapter_num": 4,
        "title": "Data",
        "subtitle": "NCERT Class 6 Mathematics • Chapter 4 Interactive Master Laboratory",
        "mentors": "Prof. P. C. Mahalanobis & Florence Nightingale",
        "mentors_title": "Pioneers of Modern Statistical Science & Visual Infographics",
        "badge": "Ganita Prakash • Statistical Literacy",
        "total_slides": 20,
        "checkpoints_count": 32,
        "quiz_questions_count": 40,
    }

    SLIDES = [
        # Slide 1: 4.1 What is Data? Collection & Purpose
        {
            "id": 1,
            "slide_num": 1,
            "title": "Data Basics",
            "subtitle": "Collection, Facts & Purpose",
            "badge": "Data Foundations",
            "summary": "Data is any collection of facts, numbers, measures, observations, or descriptions gathered to answer questions and make decisions. From student favorite sports to weather records, raw data provides the raw ingredients for informed reasoning.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Every day, we make decisions based on information: What game does our class want to play? Which book is most borrowed from the library? What was the hottest day this month? All these questions begin with <strong class="text-amber-300">data</strong>.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📋</span> What Counts as Data?
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• <strong class="text-slate-100">Definition:</strong> Any collection of facts, measurements, or observations gathered systematically.</li>
                <li>• <strong class="text-slate-100">Numerical Data:</strong> Heights in centimeters, test scores, monthly rainfall in millimeters.</li>
                <li>• <strong class="text-slate-100">Categorical Data:</strong> Favorite ice cream flavor, mode of travel to school (bus, bicycle, walk).</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30">
            <h5 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🎯</span> The Collection Process
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Step 1: <strong class="text-cyan-300">Formulate the Question:</strong> e.g., "What is the most popular sport among Grade 6 students?"</li>
                <li>• Step 2: <strong class="text-emerald-300">Gather Unbiased Responses:</strong> Survey every student once and record the raw answers.</li>
                <li>• Step 3: <strong class="text-amber-300">Raw Data vs Organized Data:</strong> Unsorted lists are confusing; organizing them into tables unlocks meaning!</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200">
        💡 <strong>Father of Indian Statistics:</strong> Professor P. C. Mahalanobis founded the Indian Statistical Institute (ISI) in Kolkata and pioneered large-scale sample surveys across India, transforming national economic planning!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp1_1",
                    "question": "What is the definition of data in mathematics?",
                    "options": [
                        "Only numbers written in a textbook",
                        "Any collection of facts, numbers, measurements, or observations gathered to convey information",
                        "A list of names only",
                        "A completed drawing"
                    ],
                    "correct": 1,
                    "explanation": "Data encompasses numbers, facts, measurements, or descriptions collected to answer questions."
                },
                {
                    "id": "cp1_2",
                    "question": "Which of the following is an example of categorical data (as opposed to numerical measurement)?",
                    "options": [
                        "Height of a student (142 cm)",
                        "Shoe size (number 5)",
                        "Favorite color (Blue, Green, Red)",
                        "Time taken to run 100 meters (15.4 seconds)"
                    ],
                    "correct": 2,
                    "explanation": "Colors are descriptive categories or labels, not numerical quantities measured on a continuous scale."
                }
            ]
        },

        # Slide 2: 4.1 Tally Marks & Frequency
        {
            "id": 2,
            "slide_num": 2,
            "title": "Tally Counts",
            "subtitle": "Grouping by Fives & Counting Occurrences",
            "badge": "Organization",
            "summary": "Tally marks provide an efficient, error-free method to record survey counts on the fly. By drawing 4 vertical strokes and a diagonal cross for the 5th mark, counts group neatly into bunches of five. Frequency is the total count in each category.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        When collecting survey data in a busy classroom, counting tick marks one by one leads to mistakes. Mathematicians use <strong class="text-amber-300">tally marks</strong> grouped into bundles of five for rapid, reliable counting.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🥢</span> The Bundle-of-Five Rule
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Count 1 to 4: Draw one vertical stroke for each response: <span class="font-mono text-cyan-300 font-bold">| , || , ||| , ||||</span>.</li>
                <li>• Count 5: Draw a diagonal slash across the four strokes: <strong class="text-amber-300 font-mono"><s>||||</s></strong> (one full bundle of 5!).</li>
                <li>• Count 6 to 9: Start new vertical strokes beside the bundle: <span class="font-mono text-slate-200"><s>||||</s> |</span> = 6.</li>
                <li>• Count 10: Two complete bundles: <span class="font-mono text-emerald-300"><s>||||</s>  <s>||||</s></span>.</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30">
            <h5 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📊</span> What is Frequency?
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• <strong class="text-cyan-300">Frequency:</strong> The total number of times a particular observation, item, or response occurs.</li>
                <li>• Example: If 12 students choose Cricket, the frequency of Cricket is <strong class="text-amber-300 font-mono">12</strong> (represented as <s>||||</s> <s>||||</s> ||).</li>
                <li>• The sum of all frequencies must equal the total number of survey participants!</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200">
        💡 <strong>Counting Shortcut:</strong> Because each crossed bundle equals 5, counting tally totals is as easy as skip-counting by fives: 5, 10, 15, 20... then adding the remaining single marks!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp2_1",
                    "question": "How is the number 8 represented using standard tally marks?",
                    "options": [
                        "|||||||| (8 plain vertical strokes)",
                        "One bundle of 5 plus 3 vertical strokes (<s>||||</s> |||)",
                        "Two bundles of 4",
                        "One bundle of 5 plus 4 strokes"
                    ],
                    "correct": 1,
                    "explanation": "8 is grouped as 5 + 3: one full crossed bundle of 5 followed by 3 single strokes."
                },
                {
                    "id": "cp2_2",
                    "question": "In a survey of 30 students, the sum of frequencies across all sports must equal:",
                    "options": ["Exactly 30", "At least 50", "15", "Any number"],
                    "correct": 0,
                    "explanation": "The sum of all category frequencies must equal the total sample size (30 students)."
                }
            ]
        },

        # Slide 3: 4.1 Organizing Numerical Data & Letter Frequency
        {
            "id": 3,
            "slide_num": 3,
            "title": "Sorting Data",
            "subtitle": "Ascending Order & Letter Frequency in Language",
            "badge": "Sorting & Patterns",
            "summary": "Raw numbers become intuitive when sorted in ascending order. Students sort shoe sizes to quickly pinpoint minimum, maximum, and mode, and tally letter occurrences in text to uncover English language frequency patterns.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Looking at an unorganized jumble of 30 shoe sizes like <em>5, 4, 7, 5, 6, 4, 5, 8, 6, 5...</em> makes it difficult to see what is happening. By <strong class="text-amber-300">sorting into ascending order</strong>, patterns emerge immediately!
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>👟</span> Sorted Shoe Sizes Table
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Sorting yields: <span class="font-mono text-cyan-200">4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 8...</span></li>
                <li>• <strong class="text-emerald-300">Smallest Value:</strong> Instantly visible at the start (Size 4).</li>
                <li>• <strong class="text-rose-300">Largest Value:</strong> Instantly visible at the end (Size 8).</li>
                <li>• <strong class="text-amber-300">Most Common (Mode):</strong> Size 5 has the highest frequency (e.g. 10 students).</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30">
            <h5 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📰</span> Letter Frequency Activity
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Count letters in an English newspaper sentence:</li>
                <li>• Letters like <strong class="text-amber-300">E, T, A, O, I, N</strong> occur with very high frequency!</li>
                <li>• Rare letters like <strong class="text-slate-400">Q, X, Z</strong> appear almost zero times.</li>
                <li>• Codebreakers, keyboard designers (QWERTY), and Morse code creators used this exact data handling method!</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-indigo-950/20 border border-indigo-500/20 text-xs text-indigo-200">
        💡 <strong>Did You Know?</strong> In Morse code, the most frequent letter 'E' is represented by a single short dot (•), while rare letters like 'Q' require a long sequence (— — • —)! Data frequency shaped telegraph technology!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp3_1",
                    "question": "Why is sorting raw numerical measurements into ascending order helpful?",
                    "options": [
                        "It makes the numbers bigger",
                        "It makes it easy to find the minimum, maximum, and frequency of each value",
                        "It removes odd numbers",
                        "It changes the data"
                    ],
                    "correct": 1,
                    "explanation": "Ascending order groups identical numbers together and immediately reveals extremes."
                },
                {
                    "id": "cp3_2",
                    "question": "Which letter of the English alphabet has the highest frequency of occurrence in standard written text?",
                    "options": ["Letter Z", "Letter X", "Letter E", "Letter Q"],
                    "correct": 2,
                    "explanation": "Letter 'E' is statistically the most frequently occurring letter in the English language (~12.7% of all letters)."
                }
            ]
        },

        # Slide 4: 4.2 Pictographs & The Concept of Scale
        {
            "id": 4,
            "slide_num": 4,
            "title": "Picture Graphs",
            "subtitle": "Visual Icons & The Key/Scale Factor",
            "badge": "Visual Data 1",
            "summary": "A pictograph represents data using pictures or icons. Instead of reading tables of numbers, readers absorb relative comparisons at a glance. The scale or key defines how many real units a single drawn symbol represents.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        A picture is worth a thousand words—and in statistics, a <strong class="text-amber-300">pictograph</strong> is worth a thousand numbers! A pictograph uses repeated icons or symbols to display counts visually.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🔑</span> The Critical Key (Scale)
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Drawing 100 bicycles on paper is impossible.</li>
                <li>• Solution: Define a <strong class="text-cyan-300">Key</strong> where 1 symbol represents multiple items!</li>
                <li>• Example: <span class="text-amber-300 font-bold">🚲 = 10 Bicycles</span>.</li>
                <li>• To represent 40 bicycles, we simply draw <strong class="text-emerald-300">4 symbols</strong> (4 × 10 = 40).</li>
                <li>• To represent 70 bicycles, we draw <strong class="text-emerald-300">7 symbols</strong> (7 × 10 = 70).</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30">
            <h5 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>👀</span> At-a-Glance Interpretation
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Longest row of symbols = <strong class="text-amber-300">Highest count</strong>.</li>
                <li>• Shortest row of symbols = <strong class="text-rose-300">Lowest count</strong>.</li>
                <li>• Readers can instantly see which category dominates without performing mental math.</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200">
        ⚠️ <strong>Golden Rule:</strong> A pictograph without a declared Key is meaningless! Always check the Key at the top or bottom of the graph before counting symbols.
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp4_1",
                    "question": "In a pictograph where 1 book icon represents 5 library books, how many books do 6 icons represent?",
                    "options": [
                        "11 books",
                        "25 books",
                        "30 books (6 × 5 = 30)",
                        "60 books"
                    ],
                    "correct": 2,
                    "explanation": "6 icons × 5 books per icon = 30 books."
                },
                {
                    "id": "cp4_2",
                    "question": "If a factory produced 80 cars, and the key states 🚗 = 20 cars, how many car symbols must be drawn?",
                    "options": [
                        "2 symbols",
                        "4 symbols (80 ÷ 20 = 4)",
                        "8 symbols",
                        "20 symbols"
                    ],
                    "correct": 1,
                    "explanation": "80 ÷ 20 = 4 symbols."
                }
            ]
        },

        # Slide 5: 4.2 Partial Symbols in Pictographs
        {
            "id": 5,
            "slide_num": 5,
            "title": "Half Symbols",
            "subtitle": "Fractions of Scale & Limitations",
            "badge": "Pictograph Nuance",
            "summary": "When counts are not exact multiples of the scale, partial or half-symbols are drawn (e.g. half a face for 5 students when 1 symbol = 10). We explore the utility and visual limitations of drawing fractions of icons.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        What happens if your key is <strong class="text-amber-300">1 Smiley = 10 Students</strong>, but a class has <strong class="text-cyan-300">25 students</strong>? Drawing two symbols gives 20, and three symbols gives 30. We need <strong class="text-emerald-300">partial symbols</strong>!
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>✂️</span> Half-Symbols
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Full symbol: <span class="text-amber-300 font-bold">1 Symbol = 10 units</span>.</li>
                <li>• Half symbol: <span class="text-cyan-300 font-bold">1/2 Symbol = 5 units</span>.</li>
                <li>• 25 students = <strong class="text-emerald-300">2 full symbols + 1 half symbol</strong> (10 + 10 + 5 = 25).</li>
                <li>• Quarter symbol: representing 2.5 or 3 units (very tricky to draw accurately!).</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-rose-500/30">
            <h5 class="font-bold text-rose-300 text-sm mb-1.5 flex items-center gap-2">
                <span>⚠️</span> Inherent Limitations of Pictographs
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• How do you draw 27 students? 7/10 of a face is almost impossible to draw or interpret accurately.</li>
                <li>• Drawing dozens of complex figures by hand is extremely tedious and time-consuming.</li>
                <li>• For very large, diverse numbers (like census data in lakhs), pictographs become impractical.</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/20 text-xs text-cyan-200">
        💡 <strong>The Bridge to Bar Graphs:</strong> These exact limitations of pictographs led mathematicians to invent the <strong>bar graph</strong>, where continuous height accurately represents any exact number!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp5_1",
                    "question": "If 1 tree symbol represents 100 trees, what does half a tree symbol represent?",
                    "options": [
                        "10 trees",
                        "25 trees",
                        "50 trees (100 ÷ 2 = 50)",
                        "100 trees"
                    ],
                    "correct": 2,
                    "explanation": "Half of the key value: 100 ÷ 2 = 50 trees."
                },
                {
                    "id": "cp5_2",
                    "question": "Why are bar graphs preferred over pictographs for displaying complex data with values like 47, 83, and 129?",
                    "options": [
                        "Pictographs use colors",
                        "Drawing and interpreting fractional parts of symbols (like 3/10 or 7/10 of an icon) is imprecise and difficult",
                        "Bar graphs have no scale",
                        "Pictographs are only for small children"
                    ],
                    "correct": 1,
                    "explanation": "Bar graph heights can accurately represent any number on a continuous numerical axis."
                }
            ]
        },

        # Slide 6: 4.3 Bar Graphs: Structure & Scale
        {
            "id": 6,
            "slide_num": 6,
            "title": "Bar Charts",
            "subtitle": "Axes, Uniform Width & Equal Gaps",
            "badge": "Visual Data 2",
            "summary": "A bar graph represents data using rectangular bars of uniform width drawn horizontally or vertically. The length/height of each bar corresponds to its frequency based on a chosen axis scale. Gaps between bars must be uniform.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        When data sets grow large, <strong class="text-amber-300">bar graphs</strong> (column charts) provide the most versatile and precise visual tool. Let us examine the anatomical rules of a standard bar graph.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📐</span> The Three Sacred Rules of Bars
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• <strong class="text-amber-300">Rule 1: Uniform Width:</strong> All bars must have the exact same width! A wider bar falsely tricks the eye into thinking it has more value.</li>
                <li>• <strong class="text-cyan-300">Rule 2: Uniform Spacing:</strong> The gap between adjacent bars must be constant throughout.</li>
                <li>• <strong class="text-emerald-300">Rule 3: Height Proportional to Frequency:</strong> The bar height is determined strictly by the scale on the numerical axis.</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30">
            <h5 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🧭</span> The Two Axes
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• <strong class="text-slate-100">Horizontal Axis (X-axis):</strong> Typically displays the categories (e.g., Sports, Days, Fruit types).</li>
                <li>• <strong class="text-slate-100">Vertical Axis (Y-axis):</strong> Contains the numerical scale, marked in equal intervals starting from zero (e.g., 0, 10, 20, 30...).</li>
                <li>• Both axes meet at a perpendicular right angle (<strong class="text-cyan-300">90° origin</strong>).</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200">
        💡 <strong>Scale Definition:</strong> The scale tells you what 1 unit length on the grid represents (e.g., <em>1 unit length = 10 students</em> or <em>1 unit length = 100 vehicles</em>).
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp6_1",
                    "question": "What is true about the widths of bars in a mathematically correct bar graph?",
                    "options": [
                        "Bars with higher values should be wider",
                        "All bars must have the exact same uniform width",
                        "Corner bars should be thinner",
                        "Width can vary randomly"
                    ],
                    "correct": 1,
                    "explanation": "All bars must have identical widths so the reader compares height alone without area distortion."
                },
                {
                    "id": "cp6_2",
                    "question": "If 1 cm unit length represents 20 vehicles, how tall is a bar representing 140 vehicles?",
                    "options": [
                        "5 cm",
                        "6 cm",
                        "7 cm (140 ÷ 20 = 7 cm)",
                        "14 cm"
                    ],
                    "correct": 2,
                    "explanation": "140 ÷ 20 = 7 unit lengths (7 cm)."
                }
            ]
        },

        # Slide 7: 4.3 Reading & Interpreting Bar Graphs
        {
            "id": 7,
            "slide_num": 7,
            "title": "Reading Bars",
            "subtitle": "Finding Maxima, Minima & Comparing Intervals",
            "badge": "Analysis Skills",
            "summary": "Master the art of reading bar graphs: identifying which category has the highest or lowest frequency, reading heights against the scale, calculating differences between bars, and computing aggregate totals across categories.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Reading a bar graph requires looking horizontally across from the top of each bar to the numerical axis. Let us practice extracting precise conclusions from a graph.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🔍</span> Key Analytical Inquiries
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• <strong class="text-amber-300">Maximum Category:</strong> Look for the tallest bar (e.g. Cricket at 40 runs).</li>
                <li>• <strong class="text-cyan-300">Minimum Category:</strong> Look for the shortest bar (e.g. Tennis at 10 runs).</li>
                <li>• <strong class="text-emerald-300">Comparative Difference:</strong> How much higher is Cricket than Tennis? <span class="font-mono text-emerald-200">40 − 10 = 30 runs</span>.</li>
                <li>• <strong class="text-violet-300">Total Sum:</strong> Add the heights of all bars to find the overall sample size.</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30">
            <h5 class="font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📈</span> Real-World Example: Hourly Traffic
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Measuring vehicles crossing a bridge between 7 AM and 11 AM:</li>
                <li>• Morning Peak: 8 AM to 9 AM shows the tallest bar (commuters traveling to work/school).</li>
                <li>• Trough: 10 AM to 11 AM drops as rush hour concludes.</li>
                <li>• City planners use these bar graph insights to schedule traffic police and bus frequencies!</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-indigo-950/20 border border-indigo-500/20 text-xs text-indigo-200">
        💡 <strong>Reading Technique:</strong> Use a straight edge or ruler held horizontally from the top of a bar across to the vertical axis to avoid misreading in-between values!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp7_1",
                    "question": "If Bar A reaches height 65 and Bar B reaches height 40 on a scale of vehicles, how many more vehicles are in Category A than B?",
                    "options": [
                        "15 vehicles",
                        "20 vehicles",
                        "25 vehicles (65 − 40 = 25)",
                        "105 vehicles"
                    ],
                    "correct": 2,
                    "explanation": "Difference between category heights: 65 − 40 = 25 vehicles."
                },
                {
                    "id": "cp7_2",
                    "question": "How do you calculate the total number of items surveyed from a bar graph?",
                    "options": [
                        "Take only the tallest bar's value",
                        "Sum the values (heights) of all the individual bars together",
                        "Multiply the highest and lowest bar",
                        "Count the number of bars"
                    ],
                    "correct": 1,
                    "explanation": "Total sample size is obtained by adding the frequencies of all bars."
                }
            ]
        },

        # Slide 8: 4.4 Step-by-Step Drawing of a Bar Graph
        {
            "id": 8,
            "slide_num": 8,
            "title": "Plotting Bars",
            "subtitle": "The 4-Step Protocol: Axes, Scale, Labels & Bars",
            "badge": "Drafting Skill",
            "summary": "Constructing a bar graph follows 4 sequential steps: draw perpendicular horizontal and vertical axes, choose and mark a uniform scale starting at zero, label categories with equal spacing, and draw bars of uniform width.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Let us master the four-step engineering protocol for drafting a clean, mathematically accurate bar graph on graph paper or plain paper.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>1️⃣ & 2️⃣</span> Steps 1 & 2: Axes and Scale
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• <strong class="text-slate-100">Step 1: Draw Perpendicular Axes:</strong> Draw a horizontal baseline and a vertical baseline meeting at a 90° corner labeled '0'.</li>
                <li>• <strong class="text-slate-100">Step 2: Choose Scale:</strong> Inspect your maximum frequency (e.g. 52). Choose a convenient step like 1 unit = 10, marking 0, 10, 20, 30, 40, 50, 60.</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-emerald-500/30">
            <h5 class="font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2">
                <span>3️⃣ & 4️⃣</span> Steps 3 & 4: Categories & Bars
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• <strong class="text-slate-100">Step 3: Mark Equal Widths:</strong> Along the horizontal axis, mark equal intervals for your categories, leaving equal gaps between them.</li>
                <li>• <strong class="text-slate-100">Step 4: Draw Bars:</strong> Draw vertical rectangles up to the exact frequency height for each category. Shade or color each bar neatly!</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200">
        💡 <strong>Scale Selection Secret:</strong> If data values range from 5 to 50, use steps of 5 or 10. If values range from 100 to 1,000, use steps of 100. Always ensure the scale fits comfortably on your page!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp8_1",
                    "question": "What number should the vertical numerical scale of a standard bar graph always start from?",
                    "options": [
                        "From zero (0)",
                        "From the lowest data value (e.g. 25)",
                        "From 100",
                        "From any random number"
                    ],
                    "correct": 0,
                    "explanation": "Standard bar graphs must start at zero to avoid visual exaggeration or distortion."
                },
                {
                    "id": "cp8_2",
                    "question": "If your highest frequency is 48, which scale is most appropriate for a graph with 6 to 10 grid marks?",
                    "options": [
                        "1 unit length = 1 (needs 50 marks, too crowded)",
                        "1 unit length = 10 (needs 5 marks: 10, 20, 30, 40, 50)",
                        "1 unit length = 100 (bar is too tiny)",
                        "1 unit length = 500"
                    ],
                    "correct": 1,
                    "explanation": "A scale of 1 unit = 10 spans 0 to 50 comfortably across 5 clean grid divisions."
                }
            ]
        },

        # Slide 9: 4.4 Practical Bar Graph Examples
        {
            "id": 9,
            "slide_num": 9,
            "title": "Case Studies",
            "subtitle": "Sweet Choices, Cricket Runs & Monthly Budgets",
            "badge": "Case Studies",
            "summary": "Explore diverse real-world bar graph applications: tallying favorite sweets (Jalebi, Gulab Jamun, Rasgulla), tracking runs scored by cricket batsmen, comparing monthly household expenditures, and monitoring wildlife sanctuary populations.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Let us examine four authentic real-world contexts where bar graphs transform raw numbers into compelling, actionable insights.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🍬</span> 1. School Sweet Preferences
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Categories: <strong class="text-amber-300">Jalebi (35)</strong>, Gulab Jamun (30), Rasgulla (25), Barfi (10).</li>
                <li>• Scale: 1 unit = 5 students (spans 0 to 40).</li>
                <li>• Decision: The school canteen orders the most Jalebis for Annual Day celebrations!</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30">
            <h5 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🏏</span> 2. Cricket Team Inning Runs
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Players: Rohit (85), Virat (92), KL Rahul (45), Hardik (38).</li>
                <li>• Scale: 1 unit = 10 runs (spans 0 to 100).</li>
                <li>• Analysis: Virat scored the highest; team total = 260 runs.</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/20 text-xs text-cyan-200">
        💡 <strong>Budget Tracking:</strong> Families categorize monthly expenses into Food, Rent, Education, Transport, and Savings. A bar graph reveals instantly which sector consumes the largest budget share.
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp9_1",
                    "question": "If 35 students chose Jalebi and 10 chose Barfi, how many more students preferred Jalebi over Barfi?",
                    "options": [
                        "15 students",
                        "20 students",
                        "25 students (35 − 10 = 25)",
                        "45 students"
                    ],
                    "correct": 2,
                    "explanation": "35 − 10 = 25 more students."
                },
                {
                    "id": "cp9_2",
                    "question": "What is the primary advantage of presenting monthly family expenses in a bar graph rather than a raw receipt list?",
                    "options": [
                        "It makes the grocery bills cheaper",
                        "It allows immediate visual comparison of which expense category dominates family spending",
                        "It hides the costs",
                        "It eliminates calculations"
                    ],
                    "correct": 1,
                    "explanation": "Bar graphs allow rapid visual comparison of relative expenditures across different categories."
                }
            ]
        },

        # Slide 10: 4.5 Vertical vs. Horizontal Orientation
        {
            "id": 10,
            "slide_num": 10,
            "title": "Chart Layout",
            "subtitle": "Vertical Columns vs Horizontal Bars",
            "badge": "Design Logic",
            "summary": "Should bars be drawn vertically or horizontally? Vertical bars suit upward-growing quantities like mountain heights or tree growth, while horizontal bars suit ground-parallel measurements like river lengths, race times, and long category names.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Did you know that bars can be drawn either standing upright (<strong class="text-amber-300">vertical columns</strong>) or lying flat (<strong class="text-cyan-300">horizontal bars</strong>)? Choosing the right orientation makes graphs intuitive and easy to read.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🏔️</span> When to Use Vertical Bars
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Best for quantities that naturally grow <strong class="text-amber-300">upward from the ground</strong>.</li>
                <li>• Examples: Mountain heights (Everest 8,848 m, K2 8,611 m), skyscraper heights, human height over age.</li>
                <li>• Best for chronological time sequences (years: 2020, 2021, 2022, 2023 along the X-axis).</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30">
            <h5 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🌊</span> When to Use Horizontal Bars
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Best for quantities that stretch <strong class="text-cyan-300">horizontally across land</strong>.</li>
                <li>• Examples: River lengths (Ganga 2,525 km, Godavari 1,465 km), train distances, highway lengths.</li>
                <li>• <strong class="text-emerald-300">Design Advantage:</strong> When category names are very long (e.g. <em>"Thiruvananthapuram Central"</em>), horizontal bars allow labels to be read without tilting your head!</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-cyan-950/20 border border-cyan-500/20 text-xs text-cyan-200">
        💡 <strong>Mathematical Equivalence:</strong> Both vertical and horizontal bar graphs convey the exact same mathematical data; orientation is an aesthetic and communication choice!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp10_1",
                    "question": "Which orientation is most intuitive when graphing the heights of famous mountain peaks?",
                    "options": [
                        "Vertical bars (columns rising upward from a ground baseline)",
                        "Horizontal bars",
                        "Circular rings",
                        "Upside-down bars"
                    ],
                    "correct": 0,
                    "explanation": "Vertical bars mirror the real-world physical direction of mountains rising up from the ground."
                },
                {
                    "id": "cp10_2",
                    "question": "Why are horizontal bar graphs especially helpful when categories have long text names?",
                    "options": [
                        "Because horizontal bars use less ink",
                        "Because long category names can be written horizontally along the Y-axis without tilting or overlapping",
                        "Because numbers cannot be written vertically",
                        "Because horizontal bars are always longer"
                    ],
                    "correct": 1,
                    "explanation": "Horizontal orientation provides wide margin space for long category labels without awkward tilting."
                }
            ]
        },

        # Slide 11: 4.5 Infographics: Visual Storytelling
        {
            "id": 11,
            "slide_num": 11,
            "title": "Visual Stories",
            "subtitle": "Combining Art, Imagery & Statistical Rigor",
            "badge": "Visual Literacy",
            "summary": "An infographic (information graphic) merges statistical data with artistic illustrations, icons, and visual storytelling. Pioneered by Florence Nightingale, infographics make complex facts rapidly understandable to the general public.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Modern newspapers, websites, and scientific journals rarely show dry numerical tables. Instead, they present <strong class="text-amber-300">infographics</strong>—compelling combinations of data, icons, color gradients, and typography.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🎨</span> Elements of a Powerful Infographic
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• <strong class="text-amber-300">Relevant Visual Metaphors:</strong> Using water droplet silhouettes to show water consumption; tree icons for forest cover.</li>
                <li>• <strong class="text-cyan-300">Hierarchical Typography:</strong> Key numbers are huge and bold; secondary explanations are compact and neat.</li>
                <li>• <strong class="text-emerald-300">Color Coding:</strong> Distinct, accessible palettes to differentiate groups (e.g., contrasting renewable vs fossil energy).</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-violet-500/30">
            <h5 class="font-bold text-violet-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🩺</span> Florence Nightingale's Polar Area Diagram
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• In 1858, British nurse <strong class="text-violet-300">Florence Nightingale</strong> invented the 'Coxcomb' (polar area chart).</li>
                <li>• It visually proved to Parliament that far more soldiers were dying of preventable hospital infections than from battlefield wounds!</li>
                <li>• Her infographic revolutionized hospital sanitation worldwide, saving millions of lives!</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-amber-950/20 border border-amber-500/20 text-xs text-amber-200">
        💡 <strong>Statistical Art:</strong> Good infographics never sacrifice numerical truth for visual flair. The underlying mathematical scale must remain 100% honest and accurate!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp11_1",
                    "question": "What is an infographic (information graphic)?",
                    "options": [
                        "A painting with no numbers",
                        "A visual representation that combines data, statistics, graphics, and text for rapid communication",
                        "A handwritten diary entry",
                        "A photograph of a calculator"
                    ],
                    "correct": 1,
                    "explanation": "Infographics blend data with graphic design and imagery to explain complex information engagingly."
                },
                {
                    "id": "cp11_2",
                    "question": "How did Florence Nightingale use visual data graphics in 1858 to reform military hospitals?",
                    "options": [
                        "By painting hospital walls blue",
                        "By drawing polar area charts showing that poor hospital sanitation caused more deaths than combat wounds",
                        "By sending secret coded messages",
                        "By inventing the microscope"
                    ],
                    "correct": 1,
                    "explanation": "Her innovative data diagrams persuaded the government to overhaul hospital hygiene, saving countess lives."
                }
            ]
        },

        # Slide 12: 4.5 Avoiding Misleading Visual Representations
        {
            "id": 12,
            "slide_num": 12,
            "title": "Graph Traps",
            "subtitle": "Distorted Scales, Area Traps & Mathematical Honesty",
            "badge": "Critical Thinking",
            "summary": "Visual graphics can deceive if drawn carelessly or dishonestly. We examine common graphical traps: scaling widths alongside heights (area distortion), truncated baselines not starting at zero, and uneven intervals.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Data never lies—but <strong class="text-rose-400">badly drawn graphics can deceive</strong>! To become statistically literate citizens, students must learn to spot and avoid misleading visual presentations.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-rose-500/30">
            <h5 class="font-bold text-rose-300 text-sm mb-1.5 flex items-center gap-2">
                <span>⚠️</span> Trap 1: The Area Illusion
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Imagine Company A sold 100 laptops and Company B sold 200 laptops (ratio 1 : 2).</li>
                <li>• An artist doubles the height AND doubles the width of Company B's laptop icon.</li>
                <li>• <strong class="text-rose-400">The Distortion:</strong> Doubling both height and width quadruples the visual area (<span class="font-mono text-rose-300">2 × 2 = 4 times bigger!</span>).</li>
                <li>• The viewer mistakenly believes Company B sold 4 times as many laptops!</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📉</span> Trap 2: Truncated Baselines
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• A graph comparing 98% vs 99% starting at baseline 95% makes 99% look twice as tall as 98%!</li>
                <li>• <strong class="text-emerald-300">Remedy:</strong> Always inspect the Y-axis. Ensure the baseline starts at zero, or clearly mark broken axis breaks (<span class="font-mono text-cyan-300">≈</span>).</li>
                <li>• Keep bar widths strictly identical. Only height should reflect value!</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200">
        💡 <strong>NCERT Guideline:</strong> In Ganita Prakash, students are cautioned: never alter the width or natural shape of objects (like stretching triangular mountains) in ways that distort underlying mathematical truth!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp12_1",
                    "question": "If you double both the height and the width of a rectangular bar representing data, by what factor does its visual area increase?",
                    "options": [
                        "2 times",
                        "3 times",
                        "4 times (2 × 2 = 4 times)",
                        "8 times"
                    ],
                    "correct": 2,
                    "explanation": "Area = width × height. Doubling both dimensions quadruples the area (4×), severely misleading the viewer."
                },
                {
                    "id": "cp12_2",
                    "question": "What happens when a bar graph's numerical scale begins at 90 instead of 0 without any break symbol?",
                    "options": [
                        "It makes the graph easier to read",
                        "Small differences (like 92 vs 96) appear gigantic and misleadingly exaggerated",
                        "The numbers become negative",
                        "It turns into a line graph"
                    ],
                    "correct": 1,
                    "explanation": "Truncating the baseline visually exaggerates minor differences, creating a false impression of huge gaps."
                }
            ]
        },

        # Slide 13: Comparative Case Study: Pictograph vs Bar Graph
        {
            "id": 13,
            "slide_num": 13,
            "title": "Chart Choice",
            "subtitle": "Choosing the Best Tool for the Context",
            "badge": "Method Selection",
            "summary": "Direct side-by-side comparison between pictographs and bar graphs. Learn which data display to choose based on audience, data precision, magnitude of counts, and communication goals.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Both pictographs and bar graphs are valuable visual tools. Which one should you pick for your school project, science report, or community presentation?
    </p>

    <div class="overflow-x-auto my-3">
        <table class="w-full text-xs text-left border-collapse border border-slate-700 bg-slate-900/90 rounded-xl overflow-hidden">
            <thead>
                <tr class="bg-slate-800 text-amber-300 border-b border-slate-700">
                    <th class="p-2.5">Feature</th>
                    <th class="p-2.5">Pictograph</th>
                    <th class="p-2.5">Bar Graph</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-800 text-slate-300">
                <tr>
                    <td class="p-2.5 font-bold text-slate-100">Representation</td>
                    <td class="p-2.5 text-cyan-300">Pictures or icons</td>
                    <td class="p-2.5 text-emerald-300">Rectangular uniform bars</td>
                </tr>
                <tr>
                    <td class="p-2.5 font-bold text-slate-100">Best Audience</td>
                    <td class="p-2.5">General public, young students, posters</td>
                    <td class="p-2.5">Scientists, engineers, business reports</td>
                </tr>
                <tr>
                    <td class="p-2.5 font-bold text-slate-100">Precision</td>
                    <td class="p-2.5 text-rose-300">Approximate (fractional symbols hard to read)</td>
                    <td class="p-2.5 text-emerald-300 font-bold">Exact & continuous numerical scale</td>
                </tr>
                <tr>
                    <td class="p-2.5 font-bold text-slate-100">Speed to Construct</td>
                    <td class="p-2.5">Slow (repeated drawings required)</td>
                    <td class="p-2.5 text-amber-300 font-bold">Rapid (drawn cleanly with a ruler)</td>
                </tr>
                <tr>
                    <td class="p-2.5 font-bold text-slate-100">Large Numbers</td>
                    <td class="p-2.5">Needs large scale (e.g. 1 icon = 10,000)</td>
                    <td class="p-2.5">Easily handles thousands, lakhs, crores</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="p-3 rounded-lg bg-indigo-950/20 border border-indigo-500/20 text-xs text-indigo-200">
        💡 <strong>Decision Rule:</strong> If you want instant visual charm for clean rounded numbers (like 10, 20, 30), a pictograph is delightful. If you need mathematical precision for exact values (like 17, 29, 43), choose a bar graph!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp13_1",
                    "question": "Which tool is superior for presenting scientific census population data with numbers like 1,42,857 and 98,421?",
                    "options": [
                        "A pictograph using stick figures",
                        "A bar graph with a calibrated scale in thousands or lakhs",
                        "A list of unorganized tally marks",
                        "A word cloud"
                    ],
                    "correct": 1,
                    "explanation": "Bar graphs handle large, precise numbers on continuous numerical axes effortlessly."
                },
                {
                    "id": "cp13_2",
                    "question": "When is a pictograph particularly effective?",
                    "options": [
                        "When numbers have many decimal places",
                        "For posters and displays intended to convey approximate comparisons quickly and engagingly to general audiences",
                        "When data contains negative numbers",
                        "When no key is provided"
                    ],
                    "correct": 1,
                    "explanation": "Pictographs excel at engaging visual appeal for general audiences comparing rounded quantities."
                }
            ]
        },

        # Slide 14: Choosing the Optimal Scale
        {
            "id": 14,
            "slide_num": 14,
            "title": "Scale Choice",
            "subtitle": "Balancing Space, Clarity & Precision",
            "badge": "Graph Optimization",
            "summary": "The choice of scale determines whether a bar graph fits neatly on a page or becomes cramped and illegible. We master selecting step intervals (1, 2, 5, 10, 20, 50, 100) based on page height and maximum frequency.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Selecting the right scale is like choosing the right magnification on a microscope. A scale that is too small makes the bars shoot off the paper; a scale that is too large squashes the bars into flat pancakes!
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📏</span> The 3-Step Scale Formula
            </h5>
            <ol class="text-xs space-y-1.5 text-slate-300 list-decimal list-inside">
                <li>Identify the <strong class="text-amber-300">Maximum Value</strong> in your data (e.g., Max = 78).</li>
                <li>Count how many grid lines (steps) fit comfortably on your page (typically 8 to 10 marks).</li>
                <li>Divide: <span class="font-mono text-cyan-200">78 ÷ 8 ≈ 9.75</span>. Round up to the nearest friendly benchmark: <strong class="text-emerald-300">1 unit = 10</strong>!</li>
            </ol>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30">
            <h5 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🌟</span> Friendly Scale Multiples
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Always choose scales in friendly multiples: <strong class="text-cyan-300">1, 2, 5, 10, 20, 50, 100, 500</strong>.</li>
                <li>• Avoid awkward scales like 1 unit = 3, 7, or 13, which make estimating intermediate heights confusing.</li>
                <li>• Clearly write your chosen scale at the top right of the graph: <em>Scale: 1 unit length = 10 students</em>.</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200">
        💡 <strong>Quick Test:</strong> If your maximum value is 380 and you have 10 marks available, what scale should you use? 380 ÷ 10 = 38 → round up to <strong>1 unit = 50</strong> (marks: 0, 50, 100, 150, 200, 250, 300, 350, 400)!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp14_1",
                    "question": "If the maximum frequency in your dataset is 94, and your vertical axis has room for 10 grid ticks, which scale is most suitable?",
                    "options": [
                        "1 unit length = 1",
                        "1 unit length = 2",
                        "1 unit length = 10 (reaching 100 in 10 ticks)",
                        "1 unit length = 100"
                    ],
                    "correct": 2,
                    "explanation": "A scale of 1 unit = 10 spans 0 to 100 in 10 ticks, comfortably covering the maximum value 94."
                },
                {
                    "id": "cp14_2",
                    "question": "Why are scale increments of 3 or 7 generally avoided when hand-drawing bar graphs?",
                    "options": [
                        "They are bad luck",
                        "They make reading intermediate in-between values difficult and prone to errors",
                        "Graph paper forbids them",
                        "They only work for fractions"
                    ],
                    "correct": 1,
                    "explanation": "Multiples of 1, 2, 5, and 10 are intuitive for humans to subdivide mentally; 3 and 7 are awkward."
                }
            ]
        },

        # Slide 15: Interpreting Double/Comparative Data
        {
            "id": 15,
            "slide_num": 15,
            "title": "Growth Trends",
            "subtitle": "Tracking Change Over Time & Categories",
            "badge": "Advanced Interpretation",
            "summary": "Learn how bar graphs illuminate trends over time (such as decade-wise population growth or term-1 vs term-2 student performance) and compare multiple data series with distinctive colors or shading.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Data becomes truly exciting when we compare how things change across <strong class="text-amber-300">time, seasons, or groups</strong>. Let us explore how bar graphs display comparative time trends.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📅</span> Decade-Wise Population Trends
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Displaying a city's population from 1990 to 2020:</li>
                <li>• 1990: 20 Lakhs | 2000: 32 Lakhs | 2010: 48 Lakhs | 2020: 65 Lakhs.</li>
                <li>• The steadily rising heights show <strong class="text-emerald-300">continuous urban growth</strong>!</li>
                <li>• You can calculate growth in each decade: 2000–2010 growth = <span class="font-mono text-cyan-200">48 − 32 = 16 Lakhs</span>.</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30">
            <h5 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🔄</span> Paired Comparison: Term 1 vs Term 2
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• Comparing student marks across two exam terms:</li>
                <li>• In Maths: Term 1 = 60, Term 2 = 85 (Growth = <strong class="text-emerald-300">+25 marks!</strong>).</li>
                <li>• In Science: Term 1 = 70, Term 2 = 78 (Growth = +8 marks).</li>
                <li>• Visual comparison highlights which subject showed the greatest improvement!</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200">
        💡 <strong>Statistical Deduction:</strong> Comparative graphs allow organizations, schools, and doctors to measure whether interventions (like study camps or fitness routines) actually produced measurable positive results.
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp15_1",
                    "question": "If a town's population was 30 lakhs in 2000 and 45 lakhs in 2010, what was the increase in population over the decade?",
                    "options": [
                        "10 lakhs",
                        "15 lakhs (45 − 30 = 15)",
                        "75 lakhs",
                        "1.5 lakhs"
                    ],
                    "correct": 1,
                    "explanation": "Population increase = 45 lakhs − 30 lakhs = 15 lakhs."
                },
                {
                    "id": "cp15_2",
                    "question": "In a comparison graph, Student A scored 62 in Term 1 and 84 in Term 2 in English. In which term was their performance higher, and by how much?",
                    "options": [
                        "Term 1 by 22 marks",
                        "Term 2 by 22 marks (84 − 62 = 22)",
                        "Both terms were equal",
                        "Term 2 by 12 marks"
                    ],
                    "correct": 1,
                    "explanation": "84 − 62 = 22 marks improvement in Term 2."
                }
            ]
        },

        # Slide 16: Grand Synthesis: The Data Life Cycle
        {
            "id": 16,
            "slide_num": 16,
            "title": "Data Cycle",
            "subtitle": "Collection, Tally, Pictograph, Bar Graph & Inferences",
            "badge": "Chapter Synthesis",
            "summary": "Review the complete 5-stage Data Life Cycle: Collection of raw data, Organization via tally marks, Visual display via pictographs and bar graphs, Critical aesthetic evaluation, and Drawing evidence-based conclusions.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Congratulations! You have mastered the complete journey of <strong class="text-amber-300">Data Handling and Presentation</strong>. Let us review the five interconnected stages of statistical investigation.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 my-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-amber-500/30">
            <h5 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🔄</span> The 5-Stage Data Cycle
            </h5>
            <ol class="text-xs space-y-1.5 text-slate-300 list-decimal list-inside">
                <li><strong class="text-amber-300">Collect:</strong> Gather accurate, unbiased observations from surveys or experiments.</li>
                <li><strong class="text-cyan-300">Organize:</strong> Tally responses in bundles of five (<s>||||</s>) and create frequency tables.</li>
                <li><strong class="text-emerald-300">Display:</strong> Select pictographs for charm or bar graphs for precision.</li>
                <li><strong class="text-violet-300">Format:</strong> Ensure uniform bar widths, equal gaps, and baseline starting at 0.</li>
                <li><strong class="text-yellow-300">Infer:</strong> Identify maxima, minima, trends, and make informed real-world decisions!</li>
            </ol>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-cyan-500/30">
            <h5 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🛡️</span> Your Statistical Superpower
            </h5>
            <ul class="text-xs space-y-1.5 text-slate-300">
                <li>• In a world filled with advertisements and online media, you can now critically examine graphs!</li>
                <li>• Check the key, verify the scale, ensure baselines start at zero, and guard against area distortion.</li>
                <li>• Use data to tell truthful, inspiring stories that improve your school and community.</li>
            </ul>
        </div>
    </div>

    <div class="p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/20 text-xs text-emerald-200">
        🎉 <strong>Ready for the Mastery Challenge?</strong> Prove your command of tallies, pictographs, bar graph drafting, and statistical reasoning across 40 questions in the four challenge arenas that follow!
    </div>
</div>
""",
            "checkpoints": [
                {
                    "id": "cp16_1",
                    "question": "What is the correct logical order of the stages in a statistical investigation?",
                    "options": [
                        "Draw Graph → Collect Data → Guess Results",
                        "Collect Data → Organize with Tallies → Display Visually → Interpret & Make Inferences",
                        "Interpret → Draw Graph → Tally",
                        "Select Scale → Guess Data → Draw Graph"
                    ],
                    "correct": 1,
                    "explanation": "Data must first be collected, then organized into frequency tables, displayed in graphs, and interpreted."
                },
                {
                    "id": "cp16_2",
                    "question": "Which pioneer of statistics used graphical polar area charts to revolutionize hospital sanitation?",
                    "options": [
                        "Florence Nightingale",
                        "Carl Friedrich Gauss",
                        "D. R. Kaprekar",
                        "Euclid"
                    ],
                    "correct": 0,
                    "explanation": "Florence Nightingale pioneered statistical visual displays (infographics) to reform healthcare."
                }
            ]
        },

        # Slide 17: Quiz Challenge 1
        {
            "id": 17,
            "slide_num": 17,
            "title": "Quiz 1",
            "subtitle": "Data Collection, Tally Marks & Sorting • Questions 1 to 10",
            "badge": "Quiz Arena 1",
            "is_quiz": True,
            "quiz_range": (1, 10),
        },

        # Slide 18: Quiz Challenge 2
        {
            "id": 18,
            "slide_num": 18,
            "title": "Quiz 2",
            "subtitle": "Pictographs, Keys & Partial Symbols • Questions 11 to 20",
            "badge": "Quiz Arena 2",
            "is_quiz": True,
            "quiz_range": (11, 20),
        },

        # Slide 19: Quiz Challenge 3
        {
            "id": 19,
            "slide_num": 19,
            "title": "Quiz 3",
            "subtitle": "Bar Graphs, Scale & Interpretation • Questions 21 to 30",
            "badge": "Quiz Arena 3",
            "is_quiz": True,
            "quiz_range": (21, 30),
        },

        # Slide 20: Quiz Challenge 4
        {
            "id": 20,
            "slide_num": 20,
            "title": "Quiz 4",
            "subtitle": "Orientation, Infographics & Misleading Data • Questions 31 to 40",
            "badge": "Quiz Arena 4",
            "is_quiz": True,
            "quiz_range": (31, 40),
        },
    ]

    # 40 Questions
    QUIZ_QUESTIONS = [
        # Questions 1-10 (Challenge 1)
        {
            "id": 1,
            "challenge": 1,
            "question": "What is data defined as in mathematics?",
            "options": [
                "Any collection of numbers, facts, measurements, or observations gathered to convey information",
                "A collection of empty tables",
                "Only words in an encyclopedia",
                "A drawing tool"
            ],
            "correct": 0,
            "explanation": "Data encompasses numbers, measurements, observations, and facts collected to answer questions."
        },
        {
            "id": 2,
            "challenge": 1,
            "question": "How is the number 5 represented using standard tally marks?",
            "options": [
                "||||| (5 vertical strokes)",
                "<s>||||</s> (4 vertical strokes with a diagonal cross stroke)",
                "V",
                "||||-"
            ],
            "correct": 1,
            "explanation": "A group of 5 is marked by 4 vertical strokes crossed by a diagonal 5th stroke."
        },
        {
            "id": 3,
            "challenge": 1,
            "question": "What is the frequency of a category in a data table?",
            "options": [
                "The time taken to write the table",
                "The number of times a particular observation or choice occurs",
                "The number of letters in the category name",
                "The largest number on the page"
            ],
            "correct": 1,
            "explanation": "Frequency is the total count of occurrences for an item or category."
        },
        {
            "id": 4,
            "challenge": 1,
            "question": "How many bundles of 5 and single strokes represent the count 17 in tally marks?",
            "options": [
                "2 bundles of 5 and 7 singles",
                "3 bundles of 5 and 2 singles (3 × 5 + 2 = 17)",
                "4 bundles of 4 and 1 single",
                "1 bundle of 10 and 7 singles"
            ],
            "correct": 1,
            "explanation": "17 = 3 full bundles of 5 plus 2 single strokes: <s>||||</s> <s>||||</s> <s>||||</s> ||."
        },
        {
            "id": 5,
            "challenge": 1,
            "question": "If 24 students choose football, 12 choose cricket, and 14 choose badminton, what is the total number of students surveyed?",
            "options": [
                "36 students",
                "48 students",
                "50 students (24 + 12 + 14 = 50)",
                "60 students"
            ],
            "correct": 2,
            "explanation": "Total = 24 + 12 + 14 = 50 students."
        },
        {
            "id": 6,
            "challenge": 1,
            "question": "Which of the following is categorical data rather than numerical measurement?",
            "options": [
                "Shoe length in centimeters",
                "Weight in kilograms",
                "Preferred fruit (Mango, Apple, Banana)",
                "Daily temperature in degrees Celsius"
            ],
            "correct": 2,
            "explanation": "Preferred fruit is a qualitative category, not a numerical measurement."
        },
        {
            "id": 7,
            "challenge": 1,
            "question": "When sorting 20 numerical test scores into ascending order, where is the highest score found?",
            "options": [
                "At the very beginning",
                "At the very end (last position)",
                "In the middle",
                "It disappears"
            ],
            "correct": 1,
            "explanation": "Ascending order arranges values from lowest to highest, placing the maximum at the end."
        },
        {
            "id": 8,
            "challenge": 1,
            "question": "In English text frequency analysis, which group of letters typically exhibits the highest frequency?",
            "options": [
                "Z, Q, X, J",
                "E, T, A, O, I, N",
                "B, K, V, W",
                "F, G, P, Y"
            ],
            "correct": 1,
            "explanation": "Letters E, T, A, O, I, N are the most common letters in English language text."
        },
        {
            "id": 9,
            "challenge": 1,
            "question": "Who was the renowned Indian scientist who founded the Indian Statistical Institute and pioneered nationwide sample surveys?",
            "options": [
                "Prof. P. C. Mahalanobis",
                "C. V. Raman",
                "Homi Bhabha",
                "Jagadish Chandra Bose"
            ],
            "correct": 0,
            "explanation": "Professor Prasanta Chandra Mahalanobis is celebrated as the Father of Modern Indian Statistics."
        },
        {
            "id": 10,
            "challenge": 1,
            "question": "In a survey of 40 students, 18 have size 5 shoes, 12 have size 6, 6 have size 4, and 4 have size 7. What is the most common shoe size (mode)?",
            "options": [
                "Size 4",
                "Size 5 (frequency = 18)",
                "Size 6",
                "Size 7"
            ],
            "correct": 1,
            "explanation": "Size 5 has the highest frequency (18 students), making it the most common value."
        },

        # Questions 11-20 (Challenge 2)
        {
            "id": 11,
            "challenge": 2,
            "question": "What is a pictograph?",
            "options": [
                "A painting with watercolors",
                "A representation of data using pictures, icons, or symbols of objects",
                "A photograph taken with a camera",
                "A type of alphabet"
            ],
            "correct": 1,
            "explanation": "A pictograph displays data visually using pictures or icons."
        },
        {
            "id": 12,
            "challenge": 2,
            "question": "In a pictograph, what does the 'Key' or 'Scale' tell the reader?",
            "options": [
                "The name of the artist",
                "How many real items or units each drawn symbol represents",
                "The date the graph was drawn",
                "The cost of the paper"
            ],
            "correct": 1,
            "explanation": "The Key specifies the ratio of real items represented by each drawn symbol."
        },
        {
            "id": 13,
            "challenge": 2,
            "question": "If 1 tree icon represents 25 trees planted, how many trees do 4 full icons represent?",
            "options": [
                "50 trees",
                "75 trees",
                "100 trees (4 × 25 = 100)",
                "125 trees"
            ],
            "correct": 2,
            "explanation": "4 icons × 25 trees/icon = 100 trees."
        },
        {
            "id": 14,
            "challenge": 2,
            "question": "If 1 circle icon represents 10 students, what does half a circle icon represent?",
            "options": [
                "2 students",
                "5 students (10 ÷ 2 = 5)",
                "10 students",
                "20 students"
            ],
            "correct": 1,
            "explanation": "Half of the key value: 10 ÷ 2 = 5 students."
        },
        {
            "id": 15,
            "challenge": 2,
            "question": "If 1 kite symbol represents 100 kites, how would 350 kites be represented in a pictograph?",
            "options": [
                "3 full kites and 1 half kite (300 + 50 = 350)",
                "2 full kites",
                "4 full kites",
                "35 kites"
            ],
            "correct": 0,
            "explanation": "3 full kites (3 × 100 = 300) plus 1 half kite (50) = 350 kites."
        },
        {
            "id": 16,
            "challenge": 2,
            "question": "What is a major limitation of pictographs when dealing with precise counts like 43 or 79?",
            "options": [
                "Pictographs cannot use colors",
                "Drawing and interpreting fractional parts of icons (like 3/10 or 9/10 of a symbol) is imprecise and hard to read",
                "Pictographs take up too little space",
                "Icons cannot be counted"
            ],
            "correct": 1,
            "explanation": "Accurately depicting and reading fractional symbols (like 3/10 of an icon) is very difficult."
        },
        {
            "id": 17,
            "challenge": 2,
            "question": "In a pictograph, Row A has 8 smiley faces and Row B has 5 smiley faces. If 1 smiley = 4 children, how many more children are in Row A than Row B?",
            "options": [
                "3 children",
                "12 children ((8 − 5) × 4 = 12)",
                "20 children",
                "32 children"
            ],
            "correct": 1,
            "explanation": "Difference in icons = 8 − 5 = 3 icons. 3 × 4 = 12 children."
        },
        {
            "id": 18,
            "challenge": 2,
            "question": "Why must symbols in a pictograph be drawn with uniform size?",
            "options": [
                "So that the paper does not rip",
                "Because drawing larger symbols for some rows would visually mislead the reader into thinking there are more items",
                "To make the drawing fast",
                "Because math rulers require it"
            ],
            "correct": 1,
            "explanation": "Varying icon size distorts visual area, misleading the viewer."
        },
        {
            "id": 19,
            "challenge": 2,
            "question": "If a pictograph displays 5 full bicycle icons and the key states 🚲 = 20 bicycles, how many bicycles were sold?",
            "options": [
                "25 bicycles",
                "80 bicycles",
                "100 bicycles (5 × 20 = 100)",
                "120 bicycles"
            ],
            "correct": 2,
            "explanation": "5 × 20 = 100 bicycles."
        },
        {
            "id": 20,
            "challenge": 2,
            "question": "Can categories in a pictograph be arranged vertically as well as horizontally?",
            "options": [
                "Only horizontally",
                "Only vertically",
                "Yes, categories can be listed horizontally or vertically depending on page space",
                "Neither"
            ],
            "correct": 2,
            "explanation": "Pictographs can arrange rows horizontally or columns vertically."
        },

        # Questions 21-30 (Challenge 3)
        {
            "id": 21,
            "challenge": 3,
            "question": "What are the bars in a mathematically correct bar graph required to have?",
            "options": [
                "Different widths for different numbers",
                "Uniform width throughout and equal spacing between adjacent bars",
                "No spaces between bars",
                "Curved edges"
            ],
            "correct": 1,
            "explanation": "Bars must have uniform width and equal spaces between them."
        },
        {
            "id": 22,
            "challenge": 3,
            "question": "In a vertical bar graph (column chart), which axis displays the numerical scale?",
            "options": [
                "The horizontal axis (X-axis)",
                "The vertical axis (Y-axis)",
                "The top border",
                "Both axes"
            ],
            "correct": 1,
            "explanation": "In vertical bar graphs, the numerical scale runs along the vertical Y-axis."
        },
        {
            "id": 23,
            "challenge": 3,
            "question": "If the scale of a bar graph is '1 unit length = 10 students', how tall is a bar representing 65 students?",
            "options": [
                "6.0 unit lengths",
                "6.5 unit lengths (65 ÷ 10 = 6.5)",
                "7.0 unit lengths",
                "65 unit lengths"
            ],
            "correct": 1,
            "explanation": "65 ÷ 10 = 6.5 unit lengths."
        },
        {
            "id": 24,
            "challenge": 3,
            "question": "What is the angle between the horizontal axis and the vertical axis in a standard bar graph?",
            "options": [
                "45°",
                "60°",
                "90° (perpendicular right angle)",
                "180°"
            ],
            "correct": 2,
            "explanation": "The two axes are perpendicular, meeting at a 90° right angle."
        },
        {
            "id": 25,
            "challenge": 3,
            "question": "On a bar graph, Bar A represents 40 runs, Bar B represents 75 runs, and Bar C represents 60 runs. What is the total runs scored?",
            "options": [
                "135 runs",
                "165 runs",
                "175 runs (40 + 75 + 60 = 175)",
                "180 runs"
            ],
            "correct": 2,
            "explanation": "40 + 75 + 60 = 175 runs."
        },
        {
            "id": 26,
            "challenge": 3,
            "question": "In a bar graph tracking hourly traffic on a highway, what does the tallest bar represent?",
            "options": [
                "The hour with the fewest cars",
                "The peak traffic hour with the highest vehicle flow",
                "The speed limit",
                "The width of the bridge"
            ],
            "correct": 1,
            "explanation": "The tallest bar corresponds to the maximum frequency (peak traffic)."
        },
        {
            "id": 27,
            "challenge": 3,
            "question": "What is the first step in drawing a bar graph?",
            "options": [
                "Color the bars",
                "Draw two perpendicular axes and label them",
                "Pick any random height",
                "Write the conclusion"
            ],
            "correct": 1,
            "explanation": "Step 1 is drawing the perpendicular horizontal and vertical reference axes."
        },
        {
            "id": 28,
            "challenge": 3,
            "question": "If your data frequencies are 150, 320, 480, and 610, which scale is most appropriate for a graph with 8 to 10 divisions?",
            "options": [
                "1 unit length = 1",
                "1 unit length = 10",
                "1 unit length = 100 (reaches 700 in 7 divisions)",
                "1 unit length = 1000"
            ],
            "correct": 2,
            "explanation": "1 unit = 100 spans 0 to 700 across 7 clean marks, fitting 610 perfectly."
        },
        {
            "id": 29,
            "challenge": 3,
            "question": "What should the baseline value of the numerical axis be in a standard bar graph?",
            "options": [
                "Zero (0)",
                "The minimum data value (e.g. 150)",
                "10",
                "Any number"
            ],
            "correct": 0,
            "explanation": "The baseline must start at zero to avoid visual scale distortion."
        },
        {
            "id": 30,
            "challenge": 3,
            "question": "If Bar X has length 8 cm and Bar Y has length 5 cm on a scale where 1 cm = 12 kg, what is the weight difference between X and Y?",
            "options": [
                "24 kg",
                "36 kg ((8 − 5) × 12 = 36 kg)",
                "48 kg",
                "60 kg"
            ],
            "correct": 1,
            "explanation": "(8 − 5) cm = 3 cm difference. 3 cm × 12 kg/cm = 36 kg."
        },

        # Questions 31-40 (Challenge 4)
        {
            "id": 31,
            "challenge": 4,
            "question": "Why are horizontal bar graphs often preferred when categories have long names (like names of Indian states)?",
            "options": [
                "Horizontal bars take less ink",
                "Long names can be read horizontally along the vertical axis without tilting or crowding",
                "Vertical bars cannot show text",
                "Horizontal graphs are always more accurate"
            ],
            "correct": 1,
            "explanation": "Horizontal layout provides generous margin space for long category labels without awkward text rotation."
        },
        {
            "id": 32,
            "challenge": 4,
            "question": "Which real-world measurement is most intuitively displayed using vertical column bars?",
            "options": [
                "Lengths of rivers",
                "Heights of mountains (growing upward from ground level)",
                "Distance between railway stations",
                "Widths of roads"
            ],
            "correct": 1,
            "explanation": "Mountain heights physically rise vertically upward from ground level."
        },
        {
            "id": 33,
            "challenge": 4,
            "question": "What is an infographic?",
            "options": [
                "A visual display combining artistic design, imagery, and statistical data for rapid understanding",
                "An encrypted computer code",
                "A black and white receipt",
                "A math exam"
            ],
            "correct": 0,
            "explanation": "An infographic blends graphic design and imagery with statistical data."
        },
        {
            "id": 34,
            "challenge": 4,
            "question": "Why is it mathematically misleading to double both the width and the height of a bar or icon when a quantity doubles?",
            "options": [
                "Because the color changes",
                "Because doubling both width and height quadruples the visual area (2 × 2 = 4 times), exaggerating the comparison",
                "Because rulers cannot measure area",
                "Because width has no effect"
            ],
            "correct": 1,
            "explanation": "Doubling two dimensions quadruples the area (4×), deceiving the viewer's eyes."
        },
        {
            "id": 35,
            "challenge": 4,
            "question": "What is a 'truncated graph' and why can it be misleading?",
            "options": [
                "A graph drawn in pencil",
                "A graph whose axis does not start at zero, exaggerating minor differences into huge visual gaps",
                "A graph with 3D shadows",
                "A graph with too many colors"
            ],
            "correct": 1,
            "explanation": "Omitting zero exaggerates small differences, misleading the audience."
        },
        {
            "id": 36,
            "challenge": 4,
            "question": "What famous healthcare infographic was invented by Florence Nightingale in 1858?",
            "options": [
                "The Pie Chart",
                "The Polar Area Diagram (Coxcomb chart)",
                "The Venn Diagram",
                "The Scatter Plot"
            ],
            "correct": 1,
            "explanation": "Nightingale invented the Polar Area Diagram (Coxcomb) to display hospital mortality causes."
        },
        {
            "id": 37,
            "challenge": 4,
            "question": "In a comparison of student marks, Rohan scored 70 in Term 1 and 88 in Term 2. What was his score improvement?",
            "options": [
                "8 marks",
                "12 marks",
                "18 marks (88 − 70 = 18)",
                "28 marks"
            ],
            "correct": 2,
            "explanation": "Improvement = 88 − 70 = 18 marks."
        },
        {
            "id": 38,
            "challenge": 4,
            "question": "If an artist draws a mountain chart where Mount Everest is shown with 3 times the width of Mount Fuji as well as 3 times the height, what is wrong mathematically?",
            "options": [
                "Nothing, it looks artistic",
                "The area of the mountain shape increases by 9 times (3 × 3 = 9), creating a grossly distorted visual comparison",
                "Everest is in Nepal",
                "The drawing should be in black and white"
            ],
            "correct": 1,
            "explanation": "Scaling two dimensions scales area quadratically ($3^2 = 9$), violating mathematical proportionality."
        },
        {
            "id": 39,
            "challenge": 4,
            "question": "When is a horizontal bar graph more suitable than a vertical bar graph?",
            "options": [
                "When measuring heights of trees",
                "When measuring horizontal lengths of major Indian rivers (like Ganga, Godavari, Krishna)",
                "When measuring human growth over years",
                "Never"
            ],
            "correct": 1,
            "explanation": "Rivers physically extend horizontally across land, matching horizontal bars."
        },
        {
            "id": 40,
            "challenge": 4,
            "question": "What is the ultimate goal of data handling and visual presentation?",
            "options": [
                "To confuse the reader with complex drawings",
                "To collect, organize, and visually communicate facts honestly so people can understand trends and make wise decisions",
                "To make the page look colorful",
                "To avoid writing words"
            ],
            "correct": 1,
            "explanation": "The purpose of data handling is honest, clear visual communication that empowers informed decisions."
        }
    ]

    # Serialization with Python True/False
    slides_json = json.dumps(SLIDES, indent=4, ensure_ascii=False).replace(': true,', ': True,').replace(': false,', ': False,')
    meta_json = json.dumps(CHAPTER_META, indent=4, ensure_ascii=False).replace(': true,', ': True,').replace(': false,', ': False,')
    quiz_json = json.dumps(QUIZ_QUESTIONS, indent=4, ensure_ascii=False).replace(': true,', ': True,').replace(': false,', ': False,')

    output_code = f'''"""NCERT Class 6 Mathematics Chapter 4: Data Handling and Presentation Data Module."""

CHAPTER_META = {meta_json}

SLIDES = {slides_json}

QUIZ_QUESTIONS = {quiz_json}
'''

    # Strict check for zero raw LaTeX
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for word in forbidden:
        if word in output_code:
            raise ValueError(f"CRITICAL ERROR: Found raw LaTeX '{word}' in data module!")

    # Check for surrogates
    clean_chars = [ch for ch in output_code if not (0xD800 <= ord(ch) <= 0xDFFF)]
    clean_output = ''.join(clean_chars)

    with open(".agents/class6_math_data_handling_data.py", "w", encoding="utf-8") as f:
        f.write(clean_output)

    print("Successfully generated .agents/class6_math_data_handling_data.py with 20 slides and 40 questions.")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in data module!")

if __name__ == "__main__":
    generate_data()

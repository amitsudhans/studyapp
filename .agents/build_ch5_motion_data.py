import re
import sys

def verify_no_latex(text, context=""):
    matches = re.findall(r'\\[a-zA-Z]+', text)
    if matches:
        print(f"ERROR: Raw LaTeX found in {context}: {matches[:10]}")
        sys.exit(1)

slides = [
    {
        "id": 1,
        "title": "Why We Measure",
        "subtitle": "Deepa's Story: Traditional Body Units vs Precise Measuring Tapes",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30 shadow-lg">
        <h4 class="text-indigo-400 font-bold text-base mb-2 flex items-center gap-2">
            <span>✂️</span> Deepa at the Tailor Shop
        </h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Deepa visits a tailor shop to get a new school uniform stitched. Her mother estimates the cloth length using <strong>char angula</strong> (four-finger width) and handspans.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            The tailor, however, uses a calibrated, flexible <strong>measuring tape</strong>. He takes exact measurements of Deepa's shoulder width, sleeve length, and height to cut fabric with flawless precision.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30 shadow-lg">
        <h4 class="text-amber-400 font-bold text-base mb-2 flex items-center gap-2">
            <span>🗣️</span> The Friends' Classroom Inquiry
        </h4>
        <ul class="text-slate-300 text-sm space-y-2">
            <li class="flex items-start gap-2">
                <span class="text-amber-400 font-bold">•</span>
                <span><strong>Anish & Hardeep:</strong> Wonder why carpenters use steel tapes instead of pacing with feet.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-amber-400 font-bold">•</span>
                <span><strong>Padma & Tasneem:</strong> Notice that flowers sold in garlands are measured by the cubit (forearm length).</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-amber-400 font-bold">•</span>
                <span><strong>Core Question:</strong> Can human body parts provide reliable measurements for everyone?</span>
            </li>
        </ul>
    </div>
</div>
<div class="mt-4 p-3 bg-indigo-950/40 rounded-xl border border-indigo-500/20 text-xs text-indigo-300">
    <strong>Key Takeaway:</strong> Body measurements are intuitive and accessible anywhere, but modern engineering, commerce, and scientific research demand reliable standard units that do not change from person to person.
</div>
""",
        "lecture_script": """Welcome to our exploration of measurement and motion! Think about a simple morning routine: buying vegetables by weight, walking 500 metres to school, or stitching a school uniform. When Deepa visited the tailor with her mother, her mother estimated fabric length using traditional handspans and char angula, meaning four-finger widths. But the tailor took out a marked, flexible measuring tape. Why could the tailor not simply rely on his own fingers or handspan? When Deepa discussed this with her friends Anish, Hardeep, Padma, and Tasneem, they realized that measurement touches every single aspect of human life. From building houses and sewing clothes to navigating satellites into space, humanity needs to know: how long, how tall, how fast, and how far. In this chapter, we discover how humankind transitioned from arbitrary body parts to universal scientific standards.""",
        "spoken_text": "Slide 1: Why We Measure. Deepa's Story: Traditional Body Units vs Precise Measuring Tapes. Welcome to our exploration of measurement and motion! Think about a simple morning routine: buying vegetables by weight, walking 500 metres to school, or stitching a school uniform. When Deepa visited the tailor with her mother, her mother estimated fabric length using traditional handspans and char angula, meaning four-finger widths. But the tailor took out a marked, flexible measuring tape. Why could the tailor not simply rely on his own fingers or handspan? When Deepa discussed this with her friends Anish, Hardeep, Padma, and Tasneem, they realized that measurement touches every single aspect of human life. From building houses and sewing clothes to navigating satellites into space, humanity needs to know: how long, how tall, how fast, and how far. In this chapter, we discover how humankind transitioned from arbitrary body parts to universal scientific standards.",
        "checkpoints": [
            {
                "question": "Why did the tailor use a calibrated measuring tape instead of handspans?",
                "options": ["Handspans are illegal", "Measuring tape provides standard, precise, and repeatable measurements", "Cloth cannot be touched by hands", "Tape makes the cloth longer"],
                "correct": 1,
                "explanation": "A calibrated measuring tape has fixed standard markings that give identical readings regardless of who measures.",
                "study_insight": "Handspans vary widely depending on age, height, and bone structure."
            },
            {
                "question": "What traditional body measurement refers to the width of four fingers?",
                "options": ["Balisht", "Char Angula", "Dhanusa", "Yojana"],
                "correct": 1,
                "explanation": "Char angula is a traditional Indian measurement representing the collective width of four fingers.",
                "study_insight": "Ancient artisans used angula as a quick proportional check during woodworking and sculpture."
            }
        ]
    },
    {
        "id": 2,
        "title": "Body Units & Inconsistency",
        "subtitle": "Activity 5.1: Handspans, Cubits, Footsteps & The Definition of a Unit",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-sky-500/30">
        <h4 class="text-sky-400 font-bold text-base mb-2">Activity 5.1: Measuring the Table</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Ask five different students to measure the exact same teacher's desk using their <strong>handspan (balisht)</strong>—the span from thumb tip to little finger tip when fully outstretched.
        </p>
        <div class="bg-sky-950/40 p-3 rounded-lg border border-sky-500/20 text-xs text-sky-300 space-y-1.5">
            <div><strong>Recorded Student Data:</strong></div>
            <div>• Student A (Tall): <strong>11 handspans</strong></div>
            <div>• Student B (Medium): <strong>13 handspans</strong></div>
            <div>• Student C (Short): <strong>15 handspans</strong></div>
            <div class="text-amber-300 font-bold">Conclusion: The table's physical length did not change, but the reported number changed because handspan size is not uniform!</div>
        </div>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
        <h4 class="text-indigo-400 font-bold text-base mb-2">The Scientific Anatomy of Measurement</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Every scientific measurement consists of exactly <strong>two essential parts</strong>:
        </p>
        <div class="p-3 bg-slate-900 rounded-lg border border-slate-700 space-y-2 text-xs text-slate-300">
            <div>
                <strong class="text-emerald-400">1. A Numerical Magnitude (Number):</strong> Tells us how many times the reference unit fits into the measured quantity (e.g., <strong>12</strong>).
            </div>
            <div>
                <strong class="text-indigo-400">2. A Chosen Unit (Standard Reference):</strong> A known, fixed quantity of the same kind chosen for comparison (e.g., <strong>handspan</strong> or <strong>metre</strong>).
            </div>
            <div class="pt-1 text-slate-400">
                Formula: <code>Measurement = Number x Unit</code> (e.g., <code>12 metres</code>).
            </div>
        </div>
    </div>
</div>
""",
        "lecture_script": """In ancient times, humans did not possess factory-made plastic rulers or laser tape measures. So what did they do? They used their own bodies! A handspan, known as balisht in Hindi, was the distance from the tip of the outstretched thumb to the tip of the little finger. A cubit, or hath, was the distance from the elbow to the tip of the middle finger. And footsteps, or paces, were used to measure outdoor farm boundaries. But here is the fundamental problem demonstrated in Activity 5.1: if three students measure the same classroom table, one records 11 handspans, another records 13, and a younger child records 15! The table itself never grew or shrank. The variation happened because every human hand is anatomically unique. A measurement always has two parts: a number and a unit. If the unit changes with every person, trade and science collapse into chaos. That is why standard units are essential.""",
        "spoken_text": "Slide 2: Body Units and Inconsistency. Activity 5.1: Handspans, Cubits, Footsteps and The Definition of a Unit. In ancient times, humans did not possess factory-made plastic rulers or laser tape measures. So what did they do? They used their own bodies! A handspan, known as balisht in Hindi, was the distance from the tip of the outstretched thumb to the tip of the little finger. A cubit, or hath, was the distance from the elbow to the tip of the middle finger. And footsteps, or paces, were used to measure outdoor farm boundaries. But here is the fundamental problem demonstrated in Activity 5.1: if three students measure the same classroom table, one records 11 handspans, another records 13, and a younger child records 15! The table itself never grew or shrank. The variation happened because every human hand is anatomically unique. A measurement always has two parts: a number and a unit. If the unit changes with every person, trade and science collapse into chaos. That is why standard units are essential.",
        "checkpoints": [
            {
                "question": "What are the two essential components of any physical measurement?",
                "options": ["Colour and shape", "A number and a unit", "Weight and volume", "Speed and direction"],
                "correct": 1,
                "explanation": "Every measurement requires a numerical value (magnitude) and a standard reference quantity called a unit (e.g., 5 metres).",
                "study_insight": "Writing just '5' is meaningless without specifying the unit of measure."
            },
            {
                "question": "Why did different students get different handspan counts for the same table in Activity 5.1?",
                "options": ["The table kept shrinking", "Different people have different handspan sizes", "The classroom was too dark", "Rulers were bent"],
                "correct": 1,
                "explanation": "Human hand dimensions vary from person to person, making handspans an inconsistent, non-standard unit.",
                "study_insight": "Non-standard units lead to commercial disputes and scientific error."
            }
        ]
    },
    {
        "id": 3,
        "title": "Indian Measurement Heritage",
        "subtitle": "From Lothal's Ivory Scale to Angula, Dhanusa & Yojana",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
        <h4 class="text-amber-400 font-bold text-base mb-2 flex items-center gap-2">
            <span>🏛️</span> Harappan Precision Engineering
        </h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Excavations at the ancient Indus Valley port city of <strong>Lothal (Gujarat)</strong> unearthed an intricately calibrated <strong>ivory measuring scale</strong> dating back over 4,400 years (c. 2400 BCE).
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            The markings on this scale were spaced just <strong>1.7 millimetres</strong> apart! This proves Harappan town planners and dock engineers used standardized metric-like precision to build parallel streets and modular kiln-fired brick docks.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
        <h4 class="text-emerald-400 font-bold text-base mb-2 flex items-center gap-2">
            <span>📜</span> Ancient Indian Length Hierarchy
        </h4>
        <div class="space-y-2 text-xs text-slate-300">
            <div class="p-2 bg-slate-900 rounded border border-slate-700">
                <strong class="text-emerald-300">1. Angula (Finger Width):</strong> The foundational base unit for carpentry, medical surgery tools (Sushruta Samhita), and temple iconography.
            </div>
            <div class="p-2 bg-slate-900 rounded border border-slate-700">
                <strong class="text-emerald-300">2. Dhanusa (Bow Length):</strong> Equivalent to 4 hastas (approx. 1.8 metres), used for land surveying and fortress architecture.
            </div>
            <div class="p-2 bg-slate-900 rounded border border-slate-700">
                <strong class="text-emerald-300">3. Yojana:</strong> Classical cosmic and long-distance travel unit mentioned in ancient astronomy, roughly equal to 12 to 15 kilometres.
            </div>
        </div>
    </div>
</div>
""",
        "lecture_script": """India possesses one of the world's most glorious and sophisticated histories of standardized measurement. Long before European civilizations adopted unified scales, the Harappan civilization of the Indus Valley engineered breathtaking planned cities like Mohenjo-daro, Harappa, and Lothal in Gujarat. Archaeologists at Lothal unearthed a polished ivory ruler with finely incised linear graduations spaced approximately 1.7 millimetres apart! That is smaller than one-sixteenth of an inch, representing the smallest division ever recorded in Bronze Age archaeology. Furthermore, classical Indian literature systematized units into an elegant mathematical hierarchy: from the angula, which was defined as the average width of a finger, up through the hasta (cubit), the dhanusa (bow length for land surveying), all the way to the yojana for interstate travel and astronomical distances.""",
        "spoken_text": "Slide 3: Indian Measurement Heritage. From Lothal's Ivory Scale to Angula, Dhanusa and Yojana. India possesses one of the world's most glorious and sophisticated histories of standardized measurement. Long before European civilizations adopted unified scales, the Harappan civilization of the Indus Valley engineered breathtaking planned cities like Mohenjo-daro, Harappa, and Lothal in Gujarat. Archaeologists at Lothal unearthed a polished ivory ruler with finely incised linear graduations spaced approximately 1.7 millimetres apart! That is smaller than one-sixteenth of an inch, representing the smallest division ever recorded in Bronze Age archaeology. Furthermore, classical Indian literature systematized units into an elegant mathematical hierarchy: from the angula, which was defined as the average width of a finger, up through the hasta (cubit), the dhanusa (bow length for land surveying), all the way to the yojana for interstate travel and astronomical distances.",
        "checkpoints": [
            {
                "question": "What ancient Indus Valley archaeological site revealed a precisely calibrated ivory measuring scale?",
                "options": ["Lothal", "Sarnath", "Hampi", "Kanchipuram"],
                "correct": 0,
                "explanation": "An ivory scale with precision divisions of approximately 1.7 mm was discovered at Lothal in Gujarat.",
                "study_insight": "Harappan bricks followed strict standardized dimension ratios across thousands of miles."
            },
            {
                "question": "Which ancient Indian unit was used to measure long intercity travel distances?",
                "options": ["Angula", "Balisht", "Yojana", "Char Angula"],
                "correct": 2,
                "explanation": "Yojana was an ancient Indian unit for long terrestrial distances, roughly equivalent to 12 to 15 kilometres.",
                "study_insight": "Angula was small (finger-width), while yojana spanned entire kingdoms."
            }
        ]
    },
    {
        "id": 4,
        "title": "The Metric SI Standard",
        "subtitle": "The International System of Units & The Standard Metre",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-cyan-500/30">
        <h4 class="text-cyan-400 font-bold text-base mb-2">The Need for Global Standardisation</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            In the 18th century, almost every country, province, and port city used different units for length (such as cubits, varas, leagues, and inches).
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            This caused severe confusion in international trade, shipping, and scientific collaboration. To create global uniformity, scientists established the <strong>International System of Units</strong> (abbreviated as <strong>SI</strong> from the French <em>Système International d'Unités</em>) in 1960.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
        <h4 class="text-indigo-400 font-bold text-base mb-2">The Metre: Base SI Unit of Length</h4>
        <div class="p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-xs text-indigo-300 space-y-2">
            <div>
                <strong>Symbol:</strong> Lowercase <code>m</code> (never capitalized <code>M</code>).
            </div>
            <div>
                <strong>Definition:</strong> The standard base unit of length in the SI system is the <strong>metre</strong>.
            </div>
            <div>
                <strong>Global Standard Bar:</strong> Originally preserved as a platinum-iridium bar in Paris, now defined with laser precision by the speed of light in vacuum.
            </div>
        </div>
    </div>
</div>
""",
        "lecture_script": """Imagine buying three yards of silk in London, only to find it equals a different length in Cairo, Paris, or Tokyo! By the late eighteenth century, international trade was paralyzed by hundreds of competing regional systems. A merchant could not reliably order screws, cloth, or machinery parts from another nation. To solve this once and for all, scientists worldwide convened and adopted the International System of Units, widely known as the SI system. For length, they established one single, universally respected base unit: the metre. Today, whether you are a scientist in New Delhi, a pilot in London, an astronaut aboard the International Space Station, or an engineer in Tokyo, one metre means the exact same physical length everywhere on Earth and beyond.""",
        "spoken_text": "Slide 4: The Metric SI Standard. The International System of Units and The Standard Metre. Imagine buying three yards of silk in London, only to find it equals a different length in Cairo, Paris, or Tokyo! By the late eighteenth century, international trade was paralyzed by hundreds of competing regional systems. A merchant could not reliably order screws, cloth, or machinery parts from another nation. To solve this once and for all, scientists worldwide convened and adopted the International System of Units, widely known as the SI system. For length, they established one single, universally respected base unit: the metre. Today, whether you are a scientist in New Delhi, a pilot in London, an astronaut aboard the International Space Station, or an engineer in Tokyo, one metre means the exact same physical length everywhere on Earth and beyond.",
        "checkpoints": [
            {
                "question": "What is the standard base SI unit of length across the globe?",
                "options": ["Foot", "Metre", "Inch", "Yard"],
                "correct": 1,
                "explanation": "The metre (m) is the internationally accepted SI base unit for measuring length.",
                "study_insight": "SI stands for Système International d'Unités."
            },
            {
                "question": "What is the correct scientific symbol for the metre?",
                "options": ["M", "mt", "m", "mtr"],
                "correct": 2,
                "explanation": "The SI symbol for the metre is strictly a lowercase 'm'.",
                "study_insight": "Uppercase 'M' stands for mega (million), so '10 M' is completely wrong for metres."
            }
        ]
    },
    {
        "id": 5,
        "title": "Multiples & Subunits",
        "subtitle": "Converting Kilometres, Metres, Centimetres & Millimetres",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-3 gap-3">
    <div class="bg-slate-800/80 p-3 rounded-xl border border-emerald-500/30">
        <div class="text-emerald-400 font-bold text-sm mb-1">1. Millimetre (mm)</div>
        <p class="text-xs text-slate-300 mb-1">Tiny subunit for pencil lead thickness, wire gauges, and insect wings.</p>
        <div class="font-mono text-xs text-emerald-300 font-bold">1 cm = 10 mm</div>
        <div class="font-mono text-[11px] text-slate-400">1 mm = 0.1 cm = 0.001 m</div>
    </div>
    <div class="bg-slate-800/80 p-3 rounded-xl border border-sky-500/30">
        <div class="text-sky-400 font-bold text-sm mb-1">2. Centimetre (cm)</div>
        <p class="text-xs text-slate-300 mb-1">Subunit for measuring notebooks, pens, shoes, and textbook pages.</p>
        <div class="font-mono text-xs text-sky-300 font-bold">1 m = 100 cm</div>
        <div class="font-mono text-[11px] text-slate-400">1 cm = 0.01 m</div>
    </div>
    <div class="bg-slate-800/80 p-3 rounded-xl border border-amber-500/30">
        <div class="text-amber-400 font-bold text-sm mb-1">3. Kilometre (km)</div>
        <p class="text-xs text-slate-300 mb-1">Large multiple for road trips, railway tracks, and intercity distances.</p>
        <div class="font-mono text-xs text-amber-300 font-bold">1 km = 1000 m</div>
        <div class="font-mono text-[11px] text-slate-400">1 km = 100,000 cm</div>
    </div>
</div>
<div class="mt-3 p-3 bg-slate-900 rounded-xl border border-slate-700 text-xs text-slate-300 flex justify-between items-center">
    <span><strong>Customary Unit Equivalents:</strong> 1 inch = 2.54 cm • 1 foot = 12 inches = 30.48 cm • 1 yard = 3 feet ≈ 0.914 m</span>
</div>
""",
        "lecture_script": """While the metre is our standard base unit, the universe contains objects of wildly different dimensions. You cannot measure the thickness of a mosquito's leg in metres, nor would you measure the distance from Delhi to Mumbai in millimetres! The metric system is brilliantly structured using powers of ten. For small objects, we divide one metre into 100 equal parts called centimetres. Each centimetre is further subdivided into 10 equal parts called millimetres. Look at your 15-centimetre school ruler: the tiniest little lines are spaced exactly one millimetre apart. For vast geographical distances, such as highways connecting cities, we group 1,000 metres together into one kilometre. Converting between these units is simple arithmetic: multiply or divide by 10, 100, or 1,000.""",
        "spoken_text": "Slide 5: Multiples and Subunits. Converting Kilometres, Metres, Centimetres and Millimetres. While the metre is our standard base unit, the universe contains objects of wildly different dimensions. You cannot measure the thickness of a mosquito's leg in metres, nor would you measure the distance from Delhi to Mumbai in millimetres! The metric system is brilliantly structured using powers of ten. For small objects, we divide one metre into 100 equal parts called centimetres. Each centimetre is further subdivided into 10 equal parts called millimetres. Look at your 15-centimetre school ruler: the tiniest little lines are spaced exactly one millimetre apart. For vast geographical distances, such as highways connecting cities, we group 1,000 metres together into one kilometre. Converting between these units is simple arithmetic: multiply or divide by 10, 100, or 1,000.",
        "checkpoints": [
            {
                "question": "How many millimetres are there in 1 centimetre?",
                "options": ["10 mm", "100 mm", "1,000 mm", "0.1 mm"],
                "correct": 0,
                "explanation": "1 centimetre is divided into exactly 10 equal millimetres.",
                "study_insight": "The smallest division marked on a typical school ruler is 1 mm."
            },
            {
                "question": "How many metres make up 1 kilometre?",
                "options": ["100 m", "500 m", "1,000 m", "10,000 m"],
                "correct": 2,
                "explanation": "The prefix 'kilo' means one thousand, so 1 kilometre = 1,000 metres.",
                "study_insight": "1 km equals 100,000 centimetres."
            }
        ]
    },
    {
        "id": 6,
        "title": "Choosing the Right Tool",
        "subtitle": "15-cm Rulers, Metre Rods, Flexible Tailor's Tapes & Surveyor Chains",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-teal-500/30">
        <h4 class="text-teal-400 font-bold text-base mb-2">Matching the Tool to the Object</h4>
        <ul class="text-xs text-slate-300 space-y-2">
            <li class="flex items-start gap-2">
                <span class="text-teal-400 font-bold">•</span>
                <span><strong>15-cm or 30-cm Plastic Scale:</strong> Ideal for flat, straight, handheld items (geometry figures, pencils, eraser length).</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-teal-400 font-bold">•</span>
                <span><strong>Rigid Wooden / Steel Metre Rod:</strong> Used by cloth merchants on counters to unroll and measure fabric reams.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-teal-400 font-bold">•</span>
                <span><strong>Flexible Tailor's Tape:</strong> Made of fiberglass or flexible vinyl to wrap around curved surfaces (chest girth, waist, tree trunk circumference).</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-teal-400 font-bold">•</span>
                <span><strong>Long Steel Measuring Tape:</strong> 30-metre or 50-metre coiled tape for room dimensions, sports running tracks, and building architecture.</span>
            </li>
        </ul>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-rose-500/30">
        <h4 class="text-rose-400 font-bold text-base mb-2">Why a Straight Scale Fails on Curves</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            If you try to measure the girth of a round banyan tree trunk with a stiff wooden ruler, the ruler cannot bend without snapping.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            Only a <strong>flexible measuring tape</strong> or a <strong>thread</strong> can conform closely to curved geometry without leaving gaps.
        </p>
    </div>
</div>
""",
        "lecture_script": """A good scientist always selects the appropriate tool for the job. You would never use an axe to sharpen a pencil, nor would you use a rigid 15-centimetre plastic ruler to measure the girth of a round tree trunk! If an object is straight, flat, and small, such as a notebook or pencil, a 15-centimetre scale is perfect. If you visit a textile merchant, you will see them using a rigid one-metre steel rod to quickly measure running lengths of cotton fabric. But if you are measuring your own waist, chest girth, or the perimeter of a curved football, a stiff ruler is completely useless. For curved surfaces, tailor's tapes made of flexible fiberglass ribbon hug the contours effortlessly. And for large school sports grounds or building foundations, construction workers use long 30-metre coiled steel surveyor tapes.""",
        "spoken_text": "Slide 6: Choosing the Right Tool. 15-cm Rulers, Metre Rods, Flexible Tailor's Tapes and Surveyor Chains. A good scientist always selects the appropriate tool for the job. You would never use an axe to sharpen a pencil, nor would you use a rigid 15-centimetre plastic ruler to measure the girth of a round tree trunk! If an object is straight, flat, and small, such as a notebook or pencil, a 15-centimetre scale is perfect. If you visit a textile merchant, you will see them using a rigid one-metre steel rod to quickly measure running lengths of cotton fabric. But if you are measuring your own waist, chest girth, or the perimeter of a curved football, a stiff ruler is completely useless. For curved surfaces, tailor's tapes made of flexible fiberglass ribbon hug the contours effortlessly. And for large school sports grounds or building foundations, construction workers use long 30-metre coiled steel surveyor tapes.",
        "checkpoints": [
            {
                "question": "Which measuring device is most suitable for measuring the circumference of a round tree trunk?",
                "options": ["A stiff 15-cm plastic ruler", "A flexible tailor's measuring tape", "A heavy wooden beam", "A compass needle"],
                "correct": 1,
                "explanation": "A flexible tailor's tape curves smoothly around cylindrical objects like tree trunks or body girth.",
                "study_insight": "Rigid rulers cannot bend around curved boundaries."
            },
            {
                "question": "What tool does a cloth merchant use on the counter to measure straight fabric lengths?",
                "options": ["A 1-metre rigid metal rod", "A sewing needle", "Handspans", "A pair of scissors"],
                "correct": 0,
                "explanation": "Cloth merchants use a calibrated 1-metre rigid metal rod to rapidly measure flat unrolled cloth.",
                "study_insight": "The rigid rod prevents fabric stretching or wrinkling during measurement."
            }
        ]
    },
    {
        "id": 7,
        "title": "Avoiding Parallax Error",
        "subtitle": "Position of the Eye: Direct Vertical Alignment (Position 'B')",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
        <h4 class="text-amber-400 font-bold text-base mb-2">What is Parallax Error?</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            <strong>Parallax error</strong> is the apparent shift in an object's position against a scale background caused by viewing it from an oblique or tilted angle.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            Because a standard ruler has thickness, looking at a mark from the left or right creates an angular line of sight that falls on the wrong division!
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
        <h4 class="text-emerald-400 font-bold text-base mb-2">The Three Viewing Positions</h4>
        <div class="space-y-2 text-xs text-slate-300">
            <div class="p-2 bg-rose-950/40 rounded border border-rose-500/20">
                <strong class="text-rose-300">Position 'A' (Viewed from Left):</strong> Angular skew makes the object appear slightly <em>longer</em> than it truly is (Positive Error).
            </div>
            <div class="p-2 bg-emerald-950/40 rounded border border-emerald-500/30">
                <strong class="text-emerald-300">Position 'B' (Directly Above at 90°):</strong> The eye is positioned vertically right above the reading point. <strong>Zero parallax error! True scientific reading.</strong>
            </div>
            <div class="p-2 bg-rose-950/40 rounded border border-rose-500/20">
                <strong class="text-rose-300">Position 'C' (Viewed from Right):</strong> Angular skew makes the object appear slightly <em>shorter</em> than it truly is (Negative Error).
            </div>
        </div>
    </div>
</div>
""",
        "lecture_script": """Have you ever noticed that if you look at a car's speedometer from the passenger seat, the needle seems to show a slightly different speed than what the driver sees? That optical illusion is called parallax! In laboratory measurements, parallax error is one of the most common mistakes students make. When you place a ruler next to a pencil, the ruler has a small thickness of about two millimetres. If your eye is positioned off to the left at Position A, your sight line crosses the tick mark at an angle, giving an artificially high reading. If your eye is off to the right at Position C, the reading is artificially low. The only scientifically accurate technique is Position B: your line of sight must be exactly perpendicular, forming a 90-degree vertical angle directly over the graduation mark.""",
        "spoken_text": "Slide 7: Avoiding Parallax Error. Position of the Eye: Direct Vertical Alignment Position B. Have you ever noticed that if you look at a car's speedometer from the passenger seat, the needle seems to show a slightly different speed than what the driver sees? That optical illusion is called parallax! In laboratory measurements, parallax error is one of the most common mistakes students make. When you place a ruler next to a pencil, the ruler has a small thickness of about two millimetres. If your eye is positioned off to the left at Position A, your sight line crosses the tick mark at an angle, giving an artificially high reading. If your eye is off to the right at Position C, the reading is artificially low. The only scientifically accurate technique is Position B: your line of sight must be exactly perpendicular, forming a 90-degree vertical angle directly over the graduation mark.",
        "checkpoints": [
            {
                "question": "Which eye position eliminates parallax error when reading a ruler?",
                "options": ["Slanted from the left (Position A)", "Directly vertically above the mark (Position B)", "Slanted from the right (Position C)", "Looking from underneath the table"],
                "correct": 1,
                "explanation": "Position B places the line of sight vertically at 90 degrees directly above the mark, eliminating parallax.",
                "study_insight": "Viewing from side angles A or C leads to parallax reading errors."
            },
            {
                "question": "What is parallax error caused by?",
                "options": ["A broken ruler", "Incorrect angular line of sight due to looking from the side", "The temperature of the room", "Using a metric scale"],
                "correct": 1,
                "explanation": "Parallax error arises when the eye is not positioned vertically perpendicular to the scale division.",
                "study_insight": "Always align your eye directly over the scale mark being recorded."
            }
        ]
    },
    {
        "id": 8,
        "title": "Handling Broken Zero Marks",
        "subtitle": "Damaged Ends, Non-Zero Starting Marks & Offset Subtraction",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
        <h4 class="text-indigo-400 font-bold text-base mb-2">The Common Problem: Broken Zero Edge</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            In school classrooms, the plastic zero edge of rulers frequently chips off, wears down, or snaps, making the 0.0 cm mark illegible.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            Does a broken zero mark mean the entire ruler must be thrown in the trash? <strong>No!</strong> You can still measure with 100% precision using the offset subtraction method.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
        <h4 class="text-emerald-400 font-bold text-base mb-2">The Offset Subtraction Rule</h4>
        <div class="p-3 bg-emerald-950/40 rounded-lg border border-emerald-500/20 text-xs text-emerald-300 space-y-2">
            <div>
                <strong>Step 1:</strong> Align the starting end of the object with any clear, intact whole number mark (such as <strong>1.0 cm</strong> or <strong>2.0 cm</strong>).
            </div>
            <div>
                <strong>Step 2:</strong> Read the mark at the opposite end of the object (say <strong>7.4 cm</strong>).
            </div>
            <div>
                <strong>Step 3:</strong> Calculate true length by subtracting initial mark from final mark:
            </div>
            <div class="p-2 bg-slate-900 rounded font-mono text-center font-bold text-amber-300">
                True Length = Final Reading - Initial Reading<br>
                Length = 7.4 cm - 1.0 cm = 6.4 cm
            </div>
        </div>
    </div>
</div>
""",
        "lecture_script": """Have you ever dropped your plastic pencil box and chipped the corner of your ruler right where the zero mark sits? Many students panic and think the ruler is now ruined and useless. But a true scientist knows that any point on a scale can serve as a starting line! If the zero mark is chipped or blurry, do not start at the broken edge. Instead, place the start of your pencil cleanly at the 1.0 centimetre mark, or even the 2.0 centimetre mark. Now look at where the tip of the pencil ends. If the tip aligns with 7.4 centimetres, what is the length of the pencil? It is not 7.4! You must subtract the starting offset: 7.4 centimetres minus 1.0 centimetre gives exactly 6.4 centimetres. By subtracting the initial reading from the final reading, you obtain perfectly accurate measurements every time.""",
        "spoken_text": "Slide 8: Handling Broken Zero Marks. Damaged Ends, Non-Zero Starting Marks and Offset Subtraction. Have you ever dropped your plastic pencil box and chipped the corner of your ruler right where the zero mark sits? Many students panic and think the ruler is now ruined and useless. But a true scientist knows that any point on a scale can serve as a starting line! If the zero mark is chipped or blurry, do not start at the broken edge. Instead, place the start of your pencil cleanly at the 1.0 centimetre mark, or even the 2.0 centimetre mark. Now look at where the tip of the pencil ends. If the tip aligns with 7.4 centimetres, what is the length of the pencil? It is not 7.4! You must subtract the starting offset: 7.4 centimetres minus 1.0 centimetre gives exactly 6.4 centimetres. By subtracting the initial reading from the final reading, you obtain perfectly accurate measurements every time.",
        "checkpoints": [
            {
                "question": "A student measures an eraser starting at 2.0 cm on a broken scale. The other end aligns with 5.5 cm. What is the true length of the eraser?",
                "options": ["5.5 cm", "3.5 cm", "7.5 cm", "2.0 cm"],
                "correct": 1,
                "explanation": "True Length = Final Reading - Initial Reading = 5.5 cm - 2.0 cm = 3.5 cm.",
                "study_insight": "Always subtract the starting mark when measuring from a non-zero mark."
            },
            {
                "question": "What should you do if the zero mark of a ruler is worn out or broken?",
                "options": ["Throw the ruler away immediately", "Start measuring from any clear full mark (like 1.0 cm) and subtract that value", "Guess the length by sight", "Add 10 cm to whatever you see"],
                "correct": 1,
                "explanation": "Aligning with an intact mark like 1.0 cm and subtracting the initial offset preserves total measurement accuracy.",
                "study_insight": "Offsets cancel out cleanly using simple subtraction."
            }
        ]
    },
    {
        "id": 9,
        "title": "SI Notation Rules",
        "subtitle": "Formatting Conventions, Symbol Grammar & Inclusive Tactile Scales",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-sky-500/30">
        <h4 class="text-sky-400 font-bold text-base mb-2">Scientific Writing Conventions</h4>
        <ul class="text-xs text-slate-300 space-y-2">
            <li class="flex items-start gap-2">
                <span class="text-emerald-400 font-bold">✓</span>
                <span><strong>Insert a Space:</strong> Always put a single space between the number and unit: <code>15 cm</code>, never <code>15cm</code>.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-emerald-400 font-bold">✓</span>
                <span><strong>No Plural 's' on Symbols:</strong> Symbols never take an 's'. Write <code>10 cm</code>, never <code>10 cms</code>; <code>5 m</code>, never <code>5 ms</code> (since 'ms' means milliseconds!).</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-emerald-400 font-bold">✓</span>
                <span><strong>Lowercase Unit Symbols:</strong> Write <code>m</code>, <code>cm</code>, <code>mm</code>, <code>km</code> in lowercase.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-emerald-400 font-bold">✓</span>
                <span><strong>No Trailing Periods:</strong> Do not put a full stop after a unit symbol unless it falls at the very end of a sentence.</span>
            </li>
        </ul>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-purple-500/30">
        <h4 class="text-purple-400 font-bold text-base mb-2 flex items-center gap-2">
            <span>🦯</span> Inclusive Accessibility: Tactile Scales
        </h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            How do visually challenged students measure lengths in science class?
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            Specialized <strong>tactile rulers</strong> are manufactured with raised, embossed dots and notched edges. Students glide their fingertips along the embossed ridges to read centimetre and millimetre increments independently by touch.
        </p>
    </div>
</div>
""",
        "lecture_script": """Science is a universal international language, and just like grammar in English, the SI system has strict writing rules. If you write your units incorrectly, it can completely alter the scientific meaning! First, always leave a space between the number and the unit symbol—write fifteen space centimetres, never cramming them together. Second, symbols are mathematical shorthand and never take a plural 's'. If you write ten followed by c-m-s, that is wrong. In fact, if you write five followed by m-s thinking it means five metres, a physicist will read it as five milliseconds! Third, unit symbols like metre, centimetre, and kilometre must be written in lowercase. Furthermore, modern science education is inclusive: visually challenged students use beautifully designed tactile rulers with raised embossed dots so that everyone can participate in precision measurement.""",
        "spoken_text": "Slide 9: SI Notation Rules. Formatting Conventions, Symbol Grammar and Inclusive Tactile Scales. Science is a universal international language, and just like grammar in English, the SI system has strict writing rules. If you write your units incorrectly, it can completely alter the scientific meaning! First, always leave a space between the number and the unit symbol—write fifteen space centimetres, never cramming them together. Second, symbols are mathematical shorthand and never take a plural 's'. If you write ten followed by c-m-s, that is wrong. In fact, if you write five followed by m-s thinking it means five metres, a physicist will read it as five milliseconds! Third, unit symbols like metre, centimetre, and kilometre must be written in lowercase. Furthermore, modern science education is inclusive: visually challenged students use beautifully designed tactile rulers with raised embossed dots so that everyone can participate in precision measurement.",
        "checkpoints": [
            {
                "question": "Which of the following is written according to proper SI scientific conventions?",
                "options": ["15cms.", "15 cm", "15CM", "15cm."],
                "correct": 1,
                "explanation": "'15 cm' correctly has a space between number and unit, uses lowercase 'cm', and does not include a plural 's' or trailing full stop.",
                "study_insight": "Never add an 's' to unit symbols; 'ms' means milliseconds, not metres."
            },
            {
                "question": "How do visually challenged students measure length accurately?",
                "options": ["By estimating with their footsteps", "Using tactile rulers with raised embossed markings that can be felt by touch", "By asking someone else to measure for them", "They cannot measure length"],
                "correct": 1,
                "explanation": "Tactile rulers feature embossed notches and Braille-like dots enabling independent reading by touch.",
                "study_insight": "Assistive tactile technology promotes inclusive laboratory learning."
            }
        ]
    },
    {
        "id": 10,
        "title": "Measuring Curved Lines",
        "subtitle": "Activity 5.4: Winding Rivers, Thread Mapping & Scale Straightening",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-teal-500/30">
        <h4 class="text-teal-400 font-bold text-base mb-2">The Curved Line Dilemma</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Consider measuring the length of a curved verandah arch, a winding river route drawn on a map, or the perimeter of an oval leaf.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            A straight rigid scale cannot bend along winding contours. Attempting to place a rigid scale across chords cuts across corners, drastically underestimating true path length.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
        <h4 class="text-amber-400 font-bold text-base mb-2">The Flexible Thread Technique</h4>
        <div class="p-3 bg-amber-950/40 rounded-lg border border-amber-500/20 text-xs text-amber-300 space-y-2">
            <div>
                <strong>Step 1:</strong> Tie a tiny knot at one end of a flexible piece of cotton thread to mark the origin point <code>A</code>.
            </div>
            <div>
                <strong>Step 2:</strong> Press the knot at the start of the curve. Using your thumb and forefinger, carefully guide small segments of the thread along the exact curved contour.
            </div>
            <div>
                <strong>Step 3:</strong> Mark the point where the thread reaches the curve's end <code>B</code> with ink.
            </div>
            <div>
                <strong>Step 4:</strong> Pull the thread straight and place it alongside a standard metre rule to read the exact length!
            </div>
        </div>
    </div>
</div>
""",
        "lecture_script": """Nature rarely moves in perfectly straight lines. Think about a serpentine river meandering through a valley, a curved road winding up a mountain hill station, or decorative string fairy lights draped over an arched doorway. How can you measure the length of a curved line when your ruler is completely straight and stiff? The answer is an ingenious method using a simple piece of flexible thread! In Activity 5.4, we tie a small knot at one end of a thread and place it at point A on the curve. Holding the thread down with your thumb, you trace it along small segments of the curved path, keeping the thread snug against the contour. When you reach the end point B, mark the thread with a pen. Finally, stretch the thread taut and straight against a standard metre scale. Instantly, the curved length is revealed with precision!""",
        "spoken_text": "Slide 10: Measuring Curved Lines. Activity 5.4: Winding Rivers, Thread Mapping and Scale Straightening. Nature rarely moves in perfectly straight lines. Think about a serpentine river meandering through a valley, a curved road winding up a mountain hill station, or decorative string fairy lights draped over an arched doorway. How can you measure the length of a curved line when your ruler is completely straight and stiff? The answer is an ingenious method using a simple piece of flexible thread! In Activity 5.4, we tie a small knot at one end of a thread and place it at point A on the curve. Holding the thread down with your thumb, you trace it along small segments of the curved path, keeping the thread snug against the contour. When you reach the end point B, mark the thread with a pen. Finally, stretch the thread taut and straight against a standard metre scale. Instantly, the curved length is revealed with precision!",
        "checkpoints": [
            {
                "question": "How can the length of a curved line drawn on paper be measured accurately?",
                "options": ["By bending a rigid wooden scale until it breaks", "Using a flexible thread along the curve and then measuring the straightened thread on a ruler", "By guessing based on colour", "Using an ordinary kitchen thermometer"],
                "correct": 1,
                "explanation": "A thread conforms to the curve; once straightened out against a ruler, it yields the true curve length.",
                "study_insight": "This technique is also used by cartographers to measure winding rivers on geographical maps."
            },
            {
                "question": "Why does measuring a curved path with small straight ruler chords give an incorrect result?",
                "options": ["It cuts across corners and underestimates the true curved distance", "Straight rulers absorb ink", "It makes the line disappear", "Chords are longer than curves"],
                "correct": 0,
                "explanation": "Straight chords skip the outer curvature of the curve, yielding a value shorter than the actual winding path.",
                "study_insight": "The curved contour is always longer than the direct chord line connecting points."
            }
        ]
    },
    {
        "id": 11,
        "title": "The Reference Point",
        "subtitle": "Describing Position, Coordinate Origins & Highway Milestones",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-blue-500/30">
        <h4 class="text-blue-400 font-bold text-base mb-2">What is a Reference Point?</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            To state where an object is located, you must always specify its position with respect to a fixed known landmark called the <strong>reference point</strong> (or <strong>origin</strong>).
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            If you say, <em>"The school is 2 kilometres away,"</em> that statement is incomplete! Is it 2 km from your home? From the railway station? Or from the bus depot?
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
        <h4 class="text-amber-400 font-bold text-base mb-2">Roadside Highway Milestones</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            When driving along national highways in India, yellow and white stone markers indicate numbers like <strong>DELHI 120 km</strong>.
        </p>
        <div class="p-3 bg-amber-950/40 rounded-lg border border-amber-500/20 text-xs text-amber-300">
            <strong>Reference Interpretation:</strong> Here, the city center of Delhi serves as the fixed <strong>reference point</strong>. The milestone tells drivers their current position is 120 km away from that reference origin along that highway.
        </div>
    </div>
</div>
""",
        "lecture_script": """Imagine calling a friend and saying: 'I am standing two kilometres away!' Your friend will immediately ask: 'Two kilometres from where?' Without a fixed reference point, describing position or location is utterly impossible! In physics, a reference point is a known, stationary location from which distance and direction are measured. If Deepa says her school is two kilometres north of the central railway station, the railway station is the reference point. If she describes it from her grandmother's house, the distance and direction change completely. When you travel on a national highway and see a milestone marked 'Agra 85', Agra is the reference point, telling you that your current location is eighty-five kilometres from the Agra reference post.""",
        "spoken_text": "Slide 11: The Reference Point. Describing Position, Coordinate Origins and Highway Milestones. Imagine calling a friend and saying: I am standing two kilometres away! Your friend will immediately ask: Two kilometres from where? Without a fixed reference point, describing position or location is utterly impossible! In physics, a reference point is a known, stationary location from which distance and direction are measured. If Deepa says her school is two kilometres north of the central railway station, the railway station is the reference point. If she describes it from her grandmother's house, the distance and direction change completely. When you travel on a national highway and see a milestone marked Agra 85, Agra is the reference point, telling you that your current location is eighty-five kilometres from the Agra reference post.",
        "checkpoints": [
            {
                "question": "What is a fixed point used to describe the position and distance of an object called?",
                "options": ["Reference point (origin)", "Moving point", "Focal point of light", "Linear unit"],
                "correct": 0,
                "explanation": "A reference point is a stationary landmark relative to which position, distance, and direction are determined.",
                "study_insight": "All spatial coordinates require a specified reference origin."
            },
            {
                "question": "A roadside milestone displays 'JAIPUR 45 km'. What is the reference point in this context?",
                "options": ["The car", "The city of Jaipur", "The Sun", "The driver's home"],
                "correct": 1,
                "explanation": "Jaipur is the reference point from which the remaining 45 km distance is measured.",
                "study_insight": "Highway milestones use target cities as their standard reference points."
            }
        ]
    },
    {
        "id": 12,
        "title": "Rest & Motion Defined",
        "subtitle": "Change in Position Over Time Relative to a Reference Point",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
        <h4 class="text-emerald-400 font-bold text-base mb-2 flex items-center gap-2">
            <span>🛑</span> State of Rest
        </h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            An object is said to be at <strong>rest</strong> if its position does not change with respect to its surroundings (reference point) as time passes.
        </p>
        <div class="p-2.5 bg-emerald-950/40 rounded-lg border border-emerald-500/20 text-xs text-emerald-300">
            <strong>Examples:</strong> A blackboard mounted on a classroom wall, a tree rooted in soil, or a textbook resting on a table.
        </div>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-sky-500/30">
        <h4 class="text-sky-400 font-bold text-base mb-2 flex items-center gap-2">
            <span>🏃</span> State of Motion
        </h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            An object is said to be in <strong>motion</strong> if its position continuously changes with respect to a reference point as time passes.
        </p>
        <div class="p-2.5 bg-sky-950/40 rounded-lg border border-sky-500/20 text-xs text-sky-300">
            <strong>Examples:</strong> A flying bird flapping across the sky, a football rolling across turf, or a train pulling away from a station platform.
        </div>
    </div>
</div>
""",
        "lecture_script": """Look around your room right now. What objects are stationary, and what objects are moving? In science, we define rest and motion with strict precision based on time and position. If an object does not change its position relative to a chosen reference point as seconds and minutes tick by, that object is at rest. The blackboard mounted on your classroom wall, the heavy desk, and the trees outside the window are all at rest relative to the school building. But if an object's position changes over time, it is in a state of motion. A bird flying past the window, a car cruising down the street, or the moving second-hand on a wall clock are all in motion. Notice the key words: change in position over time with respect to a reference point.""",
        "spoken_text": "Slide 12: Rest and Motion Defined. Change in Position Over Time Relative to a Reference Point. Look around your room right now. What objects are stationary, and what objects are moving? In science, we define rest and motion with strict precision based on time and position. If an object does not change its position relative to a chosen reference point as seconds and minutes tick by, that object is at rest. The blackboard mounted on your classroom wall, the heavy desk, and the trees outside the window are all at rest relative to the school building. But if an object's position changes over time, it is in a state of motion. A bird flying past the window, a car cruising down the street, or the moving second-hand on a wall clock are all in motion. Notice the key words: change in position over time with respect to a reference point.",
        "checkpoints": [
            {
                "question": "When is an object scientifically said to be in motion?",
                "options": ["When it makes a loud sound", "When its position changes relative to a reference point over time", "When it gets warmer", "When it changes colour"],
                "correct": 1,
                "explanation": "Motion is defined strictly as a change in an object's spatial position over time relative to a chosen reference frame.",
                "study_insight": "Without a change in position over time, an object is at rest."
            },
            {
                "question": "Which of the following is an example of an object at rest relative to the classroom?",
                "options": ["A student walking to the door", "A blackboard fixed firmly to the wall", "A butterfly flying in the room", "A rolling chalk piece"],
                "correct": 1,
                "explanation": "The fixed blackboard does not change its position relative to the classroom walls over time.",
                "study_insight": "Stationary objects maintain constant relative distance and direction."
            }
        ]
    },
    {
        "id": 13,
        "title": "Motion is Relative",
        "subtitle": "The Moving Bus Paradox: Simultaneous Rest & Motion",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-purple-500/30">
        <h4 class="text-purple-400 font-bold text-base mb-2">The Moving Bus Thought Experiment</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Imagine you and your friend are sitting peacefully side-by-side inside a school bus cruising down the highway at <strong>60 km/h</strong>.
        </p>
        <div class="p-3 bg-purple-950/40 rounded-lg border border-purple-500/20 text-xs text-purple-300 space-y-1.5">
            <div><strong>Are you in motion, or are you at rest?</strong></div>
            <div>• Relative to your friend sitting next to you: <strong>At Rest!</strong> Your distance and direction from your friend do not change.</div>
            <div>• Relative to a person standing by the roadside: <strong>In Rapid Motion!</strong> You are speeding past at 60 km/h along with the bus.</div>
        </div>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
        <h4 class="text-amber-400 font-bold text-base mb-2">Motion Depends on the Observer!</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            There is no such thing as 'absolute rest' in our universe!
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            Even while you sleep motionless in bed, you and your house are hurtling through space at over <strong>100,000 km/h</strong> as planet Earth orbits around the Sun! <strong>Rest and motion are always relative.</strong>
        </p>
    </div>
</div>
""",
        "lecture_script": """Here is one of the most mind-bending truths in all of science: an object can be at rest and in motion at the exact same moment! How is that possible? Consider sitting on a passenger train or school bus moving smoothly down the road. Look at the passenger sitting in the seat next to you. Are they moving? To you, they are sitting perfectly still; their position relative to your seat is not changing at all. You both appear at rest. But now look out the window at a person standing on the roadside. To that outside observer, both you and your friend are whizzing past at sixty kilometres per hour! An object at rest from one point of view is in rapid motion from another point of view. Motion is never absolute—it is always relative to the chosen reference frame.""",
        "spoken_text": "Slide 13: Motion is Relative. The Moving Bus Paradox: Simultaneous Rest and Motion. Here is one of the most mind-bending truths in all of science: an object can be at rest and in motion at the exact same moment! How is that possible? Consider sitting on a passenger train or school bus moving smoothly down the road. Look at the passenger sitting in the seat next to you. Are they moving? To you, they are sitting perfectly still; their position relative to your seat is not changing at all. You both appear at rest. But now look out the window at a person standing on the roadside. To that outside observer, both you and your friend are whizzing past at sixty kilometres per hour! An object at rest from one point of view is in rapid motion from another point of view. Motion is never absolute—it is always relative to the chosen reference frame.",
        "checkpoints": [
            {
                "question": "A passenger sitting inside a moving bus is at rest with respect to which of the following?",
                "options": ["A tree outside by the road", "A fellow passenger sitting in the next seat", "A pedestrian on the footpath", "A car driving past the bus"],
                "correct": 1,
                "explanation": "Relative to a fellow passenger inside the bus, their position remains unchanged over time, so they are at rest.",
                "study_insight": "Motion is relative to the chosen reference frame."
            },
            {
                "question": "Does any object in the universe experience 'absolute rest'?",
                "options": ["Yes, mountains on Earth", "No, rest and motion are always relative to a chosen reference frame", "Yes, sleeping humans", "Yes, locked vaults"],
                "correct": 1,
                "explanation": "Even stationary buildings on Earth are in rapid motion because Earth rotates on its axis and orbits the Sun.",
                "study_insight": "All motion in physics must be described relative to a specific reference origin."
            }
        ]
    },
    {
        "id": 14,
        "title": "Linear Motion",
        "subtitle": "Rectilinear Paths, Straight Trajectories & Everyday Examples",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-cyan-500/30">
        <h4 class="text-cyan-400 font-bold text-base mb-2">Defining Linear (Rectilinear) Motion</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            When an object moves along a <strong>straight-line path</strong>, its movement is classified as <strong>linear</strong> (or <strong>rectilinear</strong>) motion.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            In linear motion, the direction of movement does not change. Every point on the moving body travels in identical parallel straight lines.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
        <h4 class="text-indigo-400 font-bold text-base mb-2">Real-World Examples of Linear Motion</h4>
        <ul class="text-xs text-slate-300 space-y-2">
            <li class="flex items-start gap-2">
                <span class="text-indigo-400 font-bold">1.</span>
                <span><strong>Free Fall Under Gravity:</strong> A stone or ripe mango dropped from a tree falls straight down to the ground.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-indigo-400 font-bold">2.</span>
                <span><strong>March-Past on Parade:</strong> Soldiers marching in strict, unswerving straight lines on Republic Day.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-indigo-400 font-bold">3.</span>
                <span><strong>100m Sprint:</strong> Athletes sprinting at maximum speed down straight, parallel race lanes.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-indigo-400 font-bold">4.</span>
                <span><strong>Vehicle on a Highway:</strong> A car driving down a long, straight desert highway.</span>
            </li>
        </ul>
    </div>
</div>
""",
        "lecture_script": """Now let us explore the different types of motion based on the geometry of the path an object traces. The simplest and most fundamental type is linear motion, also known as rectilinear motion. This occurs whenever an object moves along a straight line without curving or turning. Think about a ripe mango that detaches from a branch: gravity pulls it straight down toward the ground in pure linear motion. When soldiers perform a march-past parade during Republic Day celebrations along Kartavya Path, their synchronized steps proceed in clean, unswerving straight lines. Similarly, sprinters competing in a 100-metre race stay strictly within their parallel straight lanes from start to finish. Whenever the path traced is a straight line, the motion is linear.""",
        "spoken_text": "Slide 14: Linear Motion. Rectilinear Paths, Straight Trajectories and Everyday Examples. Now let us explore the different types of motion based on the geometry of the path an object traces. The simplest and most fundamental type is linear motion, also known as rectilinear motion. This occurs whenever an object moves along a straight line without curving or turning. Think about a ripe mango that detaches from a branch: gravity pulls it straight down toward the ground in pure linear motion. When soldiers perform a march-past parade during Republic Day celebrations along Kartavya Path, their synchronized steps proceed in clean, unswerving straight lines. Similarly, sprinters competing in a 100-metre race stay strictly within their parallel straight lanes from start to finish. Whenever the path traced is a straight line, the motion is linear.",
        "checkpoints": [
            {
                "question": "What type of motion is exhibited by a stone falling freely from a rooftop?",
                "options": ["Circular motion", "Linear (rectilinear) motion", "Oscillatory motion", "Random motion"],
                "correct": 1,
                "explanation": "A dropped stone travels straight downwards along a vertical line under the pull of gravity.",
                "study_insight": "Straight-line movement is termed linear or rectilinear motion."
            },
            {
                "question": "Which of the following is an example of linear motion?",
                "options": ["The spinning blades of a ceiling fan", "Soldiers marching in a straight parade line", "A child swinging on a swing", "The pendulum of a grandfather clock"],
                "correct": 1,
                "explanation": "Marching soldiers advance in a straight line, which is classic linear motion.",
                "study_insight": "Circular and swinging motions involve curved or to-and-fro paths."
            }
        ]
    },
    {
        "id": 15,
        "title": "Circular & Rotational Motion",
        "subtitle": "Fixed Distances, Circular Paths & Spinning Axes",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
        <h4 class="text-emerald-400 font-bold text-base mb-2">Defining Circular Motion</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            When an object moves along a circular trajectory such that its <strong>distance from a central fixed point remains constant</strong>, it executes <strong>circular motion</strong>.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            The radius of the circular path stays fixed throughout the revolution.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-sky-500/30">
        <h4 class="text-sky-400 font-bold text-base mb-2">Everyday Circular & Rotational Systems</h4>
        <ul class="text-xs text-slate-300 space-y-2">
            <li class="flex items-start gap-2">
                <span class="text-sky-400 font-bold">•</span>
                <span><strong>Whirled Stone on a String:</strong> An eraser or pebble tied to a string and whirled overhead in a horizontal circle.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-sky-400 font-bold">•</span>
                <span><strong>Blades of a Ceiling Fan:</strong> The fan blades rotate around a central motor spindle at fixed radial distance.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-sky-400 font-bold">•</span>
                <span><strong>Hands of a Clock:</strong> The tip of the second hand traces a circular circumference around the central dial pin.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-sky-400 font-bold">•</span>
                <span><strong>Carnival Merry-Go-Round:</strong> Wooden horses revolving in circular loops at equal radial distance.</span>
            </li>
        </ul>
    </div>
</div>
""",
        "lecture_script": """What happens when the path of motion curves into a complete closed circle? That is circular motion! Imagine tying an eraser to one end of a string and whirling it around your head. As the eraser spins, its distance from your hand—which is the length of the string—remains completely constant. The eraser traces a circular path around your hand. Think about the blades of a ceiling fan in your classroom: while the central fan rod stays stationary, every point on the fan blade moves in a circle around the central hub. The same is true for the tip of the second hand on a wall clock, revolving in a continuous 360-degree circle every sixty seconds, or children giggling as they spin on a park merry-go-round. When distance from a central fixed point remains constant while moving in a loop, it is circular motion.""",
        "spoken_text": "Slide 15: Circular and Rotational Motion. Fixed Distances, Circular Paths and Spinning Axes. What happens when the path of motion curves into a complete closed circle? That is circular motion! Imagine tying an eraser to one end of a string and whirling it around your head. As the eraser spins, its distance from your hand—which is the length of the string—remains completely constant. The eraser traces a circular path around your hand. Think about the blades of a ceiling fan in your classroom: while the central fan rod stays stationary, every point on the fan blade moves in a circle around the central hub. The same is true for the tip of the second hand on a wall clock, revolving in a continuous 360-degree circle every sixty seconds, or children giggling as they spin on a park merry-go-round. When distance from a central fixed point remains constant while moving in a loop, it is circular motion.",
        "checkpoints": [
            {
                "question": "What remains constant when an object moves in uniform circular motion?",
                "options": ["Its colour", "Its distance from the fixed central pivot point", "The direction it faces", "Its weight"],
                "correct": 1,
                "explanation": "In circular motion, the object maintains a constant radial distance from the central axis.",
                "study_insight": "The radius of the circular path stays fixed."
            },
            {
                "question": "What type of motion is executed by the tip of the hands of a clock?",
                "options": ["Linear motion", "Circular motion", "Oscillatory motion", "Random motion"],
                "correct": 1,
                "explanation": "The tip of a clock hand sweeps out a circle around the central pivot pin.",
                "study_insight": "It also exhibits periodic motion because it repeats each complete cycle in fixed time."
            }
        ]
    },
    {
        "id": 16,
        "title": "Oscillatory & Periodic Motion",
        "subtitle": "To-and-Fro Vibrations, Swings, Pendulums & Periodic Cycles",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-purple-500/30">
        <h4 class="text-purple-400 font-bold text-base mb-2">Oscillatory (To-and-Fro) Motion</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            When an object moves <strong>to and fro</strong> (back and forth) about a central fixed mean position, its motion is called <strong>oscillatory motion</strong>.
        </p>
        <ul class="text-xs text-slate-300 space-y-1.5">
            <li>• <strong>Swinging Pendulum:</strong> A metal bob swinging symmetrically left and right past its lowest center point.</li>
            <li>• <strong>Playground Swing:</strong> A child swinging forwards and backwards.</li>
            <li>• <strong>Vibrating Musical Strings:</strong> Plucking the string of a sitar, guitar, or veena.</li>
        </ul>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
        <h4 class="text-amber-400 font-bold text-base mb-2">Periodic Nature of Motion</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            A motion that <strong>repeats itself after regular, fixed intervals of time</strong> is classified as <strong>periodic motion</strong>.
        </p>
        <div class="p-3 bg-amber-950/40 rounded-lg border border-amber-500/20 text-xs text-amber-300">
            <strong>Key Insight:</strong> Most oscillatory motions (like pendulums) and circular motions (like planetary orbits and clock hands) are <strong>periodic</strong> because they complete each cycle in an exact, predictable duration of time!
        </div>
    </div>
</div>
""",
        "lecture_script": """Finally, let us explore motion that repeats back and forth: oscillatory motion! When a child sits on a playground swing, they do not travel along a straight line, nor do they spin in a full 360-degree loop. Instead, they move forward, slow down, stop, reverse backward past the center, stop again, and swing forward. This to-and-fro movement about a central equilibrium position is called oscillatory motion. You see it in the swinging pendulum of an antique grandfather clock, the bobbing of a spring, the prongs of a struck tuning fork, and the vibrating strings of a sitar or guitar that produce musical notes. Now notice a vital characteristic: the pendulum swings back and forth in regular, repeatable cycles. Any motion that repeats after equal, fixed intervals of time is called periodic motion. Both circular orbits and oscillatory swings are beautiful examples of periodic motion in our cosmos.""",
        "spoken_text": "Slide 16: Oscillatory and Periodic Motion. To-and-Fro Vibrations, Swings, Pendulums and Periodic Cycles. Finally, let us explore motion that repeats back and forth: oscillatory motion! When a child sits on a playground swing, they do not travel along a straight line, nor do they spin in a full 360-degree loop. Instead, they move forward, slow down, stop, reverse backward past the center, stop again, and swing forward. This to-and-fro movement about a central equilibrium position is called oscillatory motion. You see it in the swinging pendulum of an antique grandfather clock, the bobbing of a spring, the prongs of a struck tuning fork, and the vibrating strings of a sitar or guitar that produce musical notes. Now notice a vital characteristic: the pendulum swings back and forth in regular, repeatable cycles. Any motion that repeats after equal, fixed intervals of time is called periodic motion. Both circular orbits and oscillatory swings are beautiful examples of periodic motion in our cosmos.",
        "checkpoints": [
            {
                "question": "What type of motion is exhibited by a child on a playground swing or a clock pendulum?",
                "options": ["Linear motion", "Circular motion", "Oscillatory (to-and-fro) motion", "Random motion"],
                "correct": 2,
                "explanation": "A swing moves to and fro about a central resting position, which is oscillatory motion.",
                "study_insight": "Oscillatory motion alternates direction repeatedly across a central point."
            },
            {
                "question": "What is any motion that repeats itself at regular, fixed time intervals called?",
                "options": ["Periodic motion", "Linear motion", "Curvilinear motion", "Accelerated motion"],
                "correct": 0,
                "explanation": "Motion repeating over equal time periods is periodic (e.g., Earth's rotation, swinging pendulum, heartbeat).",
                "study_insight": "Both uniform circular motion and regular oscillatory motion are periodic."
            }
        ]
    }
]

# Verify no latex in slides
for s in slides:
    verify_no_latex(s['concept_html'], f"Slide {s['id']} concept_html")
    verify_no_latex(s['lecture_script'], f"Slide {s['id']} lecture_script")
    verify_no_latex(s['spoken_text'], f"Slide {s['id']} spoken_text")
    for cp in s['checkpoints']:
        verify_no_latex(cp['question'], f"Slide {s['id']} checkpoint question")
        for opt in cp['options']:
            verify_no_latex(opt, f"Slide {s['id']} checkpoint option")
        verify_no_latex(cp['explanation'], f"Slide {s['id']} checkpoint explanation")
        verify_no_latex(cp['study_insight'], f"Slide {s['id']} checkpoint insight")

print(f"Verified {len(slides)} concept slides with zero raw LaTeX.")

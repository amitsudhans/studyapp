import re
import sys

def verify_no_latex(text, context=""):
    matches = re.findall(r'\\[a-zA-Z]+', text)
    if matches:
        print(f"ERROR: Raw LaTeX found in {context}: {matches[:10]}")
        sys.exit(1)

quiz_questions = [
    # Challenge 1 (Q1 - Q10): Slides 1-4 topics
    {
        "id": 1,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 1,
        "question": "What is the primary reason why handspans, foot lengths, and cubits are not used as standard units?",
        "options": ["They are too difficult to remember", "They vary from person to person depending on body size", "They cannot be used outdoors", "They are only used in winter"],
        "correct": 1,
        "explanation": "Human body dimensions vary between individuals, making body-part units inconsistent and non-standard.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. A handspan depends on the size of an individual's hand, which differs based on age, height, and genetics.</p>
    <p>2. If two people measure the same classroom desk, they will obtain different numbers of handspans.</p>
    <p>3. Standard units must remain constant regardless of who performs the measurement.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: They vary from person to person depending on body size</p>
</div>
"""
    },
    {
        "id": 2,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 2,
        "question": "What are the two essential components required to express any scientific measurement?",
        "options": ["A tool and a colour", "A number and a unit", "A speed and a direction", "A mass and a volume"],
        "correct": 1,
        "explanation": "Every measurement consists of a numerical magnitude (number) and a standard reference quantity (unit), such as 15 cm.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Stating only a number (e.g., '12') gives no physical meaning.</p>
    <p>2. A unit defines the standard reference against which the quantity is compared.</p>
    <p>3. Thus, a complete measurement requires both: Number x Unit (e.g., 12 metres).</p>
    <p class='text-emerald-400 font-bold'>Correct Option: A number and a unit</p>
</div>
"""
    },
    {
        "id": 3,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 3,
        "question": "Which ancient Indus Valley archaeological excavation yielded an ivory measuring scale with 1.7 mm divisions?",
        "options": ["Lothal (Gujarat)", "Sanchi (Madhya Pradesh)", "Taxila", "Konark (Odisha)"],
        "correct": 0,
        "explanation": "Archaeologists discovered an intricately calibrated ivory scale with ~1.7 mm divisions at Lothal, Gujarat.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Lothal was a major port and dockyard city of the Harappan civilization.</p>
    <p>2. The ivory scale found there dates to around 2400 BCE.</p>
    <p>3. Its 1.7 mm subdivisions demonstrate advanced ancient standardization in civic planning.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Lothal (Gujarat)</p>
</div>
"""
    },
    {
        "id": 4,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 4,
        "question": "What ancient Indian unit of length was defined based on the average width of a human finger?",
        "options": ["Yojana", "Dhanusa", "Angula", "Hasta"],
        "correct": 2,
        "explanation": "Angula was the traditional Indian unit corresponding to finger width, widely used in woodworking and sculpture.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. 'Angula' means finger in Sanskrit.</p>
    <p>2. Four finger widths formed 'char angula'.</p>
    <p>3. Larger multiples included hasta (cubit, 24 angulas) and dhanusa (bow, 4 hastas).</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Angula</p>
</div>
"""
    },
    {
        "id": 5,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 5,
        "question": "What ancient Indian unit was used to measure long intercity travel distances?",
        "options": ["Balisht", "Yojana", "Angula", "Pace"],
        "correct": 1,
        "explanation": "Yojana was an ancient Indian unit used for astronomical and long terrestrial travel distances, approximately 12 to 15 km.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Ancient texts describe kingdom boundaries and journeys in yojanas.</p>
    <p>2. One yojana is traditionally regarded as approximately 12 to 15 kilometres.</p>
    <p>3. Angula and balisht were for small, local handheld objects.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Yojana</p>
</div>
"""
    },
    {
        "id": 6,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 6,
        "question": "What does the abbreviation 'SI' in the International System of Units stand for?",
        "options": ["Standard India", "Système International d'Unités", "Scientific Index", "System of Instruments"],
        "correct": 1,
        "explanation": "SI stands for 'Système International d'Unités' (French for International System of Units), adopted globally in 1960.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The General Conference on Weights and Measures adopted the unified system in 1960.</p>
    <p>2. In French, it is titled 'Système International d'Unités'.</p>
    <p>3. The official international abbreviation in all languages is 'SI'.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Système International d'Unités</p>
</div>
"""
    },
    {
        "id": 7,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 7,
        "question": "What is the standard base SI unit of length?",
        "options": ["Kilometre", "Centimetre", "Metre", "Millimetre"],
        "correct": 2,
        "explanation": "The metre (symbol: m) is the fundamental base unit of length in the International System of Units.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The SI system has seven base units.</p>
    <p>2. For the physical quantity of length, the base unit is the metre.</p>
    <p>3. Centimetres, millimetres, and kilometres are derived prefixes (subunits and multiples).</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Metre</p>
</div>
"""
    },
    {
        "id": 8,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 8,
        "question": "Why did nations around the world agree to adopt a single international system of units (SI)?",
        "options": ["To eliminate confusion in international commerce, travel, and science", "Because rulers could only be made in France", "To make math harder for students", "Because human hands were banned"],
        "correct": 0,
        "explanation": "A unified standard ensures seamless international trade, industrial manufacturing, and scientific communication without conversion errors.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Having different units in every port caused severe commercial fraud and misunderstanding.</p>
    <p>2. Machine parts manufactured in one country could not fit equipment in another.</p>
    <p>3. Global standardization solved this by establishing identical units worldwide.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: To eliminate confusion in international commerce, travel, and science</p>
</div>
"""
    },
    {
        "id": 9,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 9,
        "question": "What traditional body unit represents the distance from the elbow to the tip of the middle finger?",
        "options": ["Handspan (Balisht)", "Cubit (Hath)", "Pace (Stride)", "Fathom"],
        "correct": 1,
        "explanation": "A cubit (or hath in Hindi) is the historical measure of length from the elbow joint to the tip of the extended middle finger.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. A handspan is from thumb tip to little finger tip.</p>
    <p>2. A cubit (hath) spans the entire forearm from elbow to middle finger tip.</p>
    <p>3. It was historically used in cloth markets and garland stalls.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Cubit (Hath)</p>
</div>
"""
    },
    {
        "id": 10,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 10,
        "question": "What is the correct scientific symbol for the SI base unit of length?",
        "options": ["M", "mt", "m", "mtr"],
        "correct": 2,
        "explanation": "The SI symbol for the metre is strictly a lowercase 'm'.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. In SI conventions, units named after common objects or non-persons are written in lowercase.</p>
    <p>2. 'M' denotes the prefix 'mega' (million).</p>
    <p>3. 'mt' or 'mtr' are non-standard informal abbreviations; 'm' is the only official symbol.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: m</p>
</div>
"""
    },

    # Challenge 2 (Q11 - Q20): Slides 5-8 topics
    {
        "id": 11,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 11,
        "question": "How many centimetres are there in 1 metre?",
        "options": ["10 cm", "100 cm", "1,000 cm", "0.01 cm"],
        "correct": 1,
        "explanation": "The prefix 'centi' means one-hundredth (1/100), meaning there are 100 centimetres in 1 metre.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. 1 metre is divided into 100 equal parts.</p>
    <p>2. Each part is called a centimetre (cm).</p>
    <p>3. Therefore: 1 m = 100 cm.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: 100 cm</p>
</div>
"""
    },
    {
        "id": 12,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 12,
        "question": "What is the smallest division typically marked on a standard 15-cm student ruler?",
        "options": ["1 centimetre", "1 millimetre", "1 metre", "1 inch"],
        "correct": 1,
        "explanation": "A standard school ruler subdivides each centimetre into 10 millimetres, so the smallest marked division is 1 mm (0.1 cm).",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. On a 15-cm scale, numbers 1, 2, 3... mark centimetres.</p>
    <p>2. Between each numbered centimetre, there are 10 small sub-divisions.</p>
    <p>3. Each tiny sub-division represents 1 millimetre (1 mm = 0.1 cm).</p>
    <p class='text-emerald-400 font-bold'>Correct Option: 1 millimetre</p>
</div>
"""
    },
    {
        "id": 13,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 13,
        "question": "A runner completes a 5-kilometre race. How many metres did the runner cover?",
        "options": ["500 m", "5,000 m", "50,000 m", "500,000 m"],
        "correct": 1,
        "explanation": "Since 1 km = 1,000 m, 5 km = 5 x 1,000 = 5,000 metres.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The prefix 'kilo' equals 1,000.</p>
    <p>2. 1 km = 1,000 m.</p>
    <p>3. Multiply: 5 km x 1,000 m/km = 5,000 m.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: 5,000 m</p>
</div>
"""
    },
    {
        "id": 14,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 14,
        "question": "How many centimetres are equivalent to 1 customary inch?",
        "options": ["1.50 cm", "2.54 cm", "3.14 cm", "5.00 cm"],
        "correct": 1,
        "explanation": "By international definition, 1 inch is exactly equal to 2.54 centimetres.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The inch is a customary Anglo-American unit of length.</p>
    <p>2. 1 inch = 2.54 cm.</p>
    <p>3. 12 inches make 1 foot (approx. 30.48 cm).</p>
    <p class='text-emerald-400 font-bold'>Correct Option: 2.54 cm</p>
</div>
"""
    },
    {
        "id": 15,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 15,
        "question": "Which measuring tool should be chosen to measure the chest girth of an athlete?",
        "options": ["A 15-cm rigid plastic scale", "A wooden metre stick", "A flexible tailor's measuring tape", "A steel surveyor chain"],
        "correct": 2,
        "explanation": "Human body curves require a flexible tailor's tape that wraps smoothly around contours without gaps.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The human torso has a curved, oval cross-section.</p>
    <p>2. Rigid scales cannot bend to conform to body curvature.</p>
    <p>3. A flexible fiberglass tailor's tape wraps cleanly around the chest to provide an accurate girth reading.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: A flexible tailor's measuring tape</p>
</div>
"""
    },
    {
        "id": 16,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 16,
        "question": "What is the proper position of the eye when taking a reading on a scale to prevent parallax error?",
        "options": ["Looking from the left side at 45 degrees", "Directly vertically above the mark at 90 degrees (Position B)", "Looking from the right side at 45 degrees", "Looking from underneath the table"],
        "correct": 1,
        "explanation": "The eye must be vertically aligned directly above the mark being read to eliminate angular parallax distortion.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Rulers have a small physical thickness.</p>
    <p>2. Viewing from an oblique angle (left or right) shifts the apparent position of the mark relative to the object.</p>
    <p>3. Aligning the eye vertically at 90 degrees (Position B) ensures zero line-of-sight deviation.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Directly vertically above the mark at 90 degrees (Position B)</p>
</div>
"""
    },
    {
        "id": 17,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 17,
        "question": "What happens if a student reads a scale with their eye positioned too far to the left (Position A)?",
        "options": ["The reading is completely accurate", "The object appears slightly longer than it truly is due to angular parallax", "The ruler becomes magnetic", "The numbers change colour"],
        "correct": 1,
        "explanation": "Viewing from the left projects an angled line of sight that crosses a higher division on the scale, causing a positive parallax error.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Looking from Position A (left angle) creates an oblique line of sight.</p>
    <p>2. The object's edge appears aligned with a tick mark further to the right.</p>
    <p>3. This produces an artificially inflated, inaccurate reading.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: The object appears slightly longer than it truly is due to angular parallax</p>
</div>
"""
    },
    {
        "id": 18,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 18,
        "question": "A student measures a pencil with a broken ruler, starting at 1.0 cm. The opposite tip reads 8.7 cm. What is the pencil's length?",
        "options": ["8.7 cm", "1.0 cm", "7.7 cm", "9.7 cm"],
        "correct": 2,
        "explanation": "True Length = Final Reading - Initial Reading = 8.7 cm - 1.0 cm = 7.7 cm.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The initial mark is 1.0 cm (not 0.0 cm).</p>
    <p>2. The final mark is 8.7 cm.</p>
    <p>3. Subtract: 8.7 cm - 1.0 cm = 7.7 cm.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: 7.7 cm</p>
</div>
"""
    },
    {
        "id": 19,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 19,
        "question": "Why should a student avoid starting a measurement at a chipped, worn-out zero edge of a scale?",
        "options": ["The chipped edge makes the pencil break", "The exact zero point cannot be seen, leading to random errors", "Zero marks carry electric shock", "Rulers are only meant to start at 5 cm"],
        "correct": 1,
        "explanation": "A worn or broken zero edge obscures the true datum point, introducing systematic measurement error.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Over time, plastic ruler ends get chipped and rounded.</p>
    <p>2. Estimating where the 0.0 mark used to be leads to inaccurate guesswork.</p>
    <p>3. Starting at an intact whole mark (like 1.0 cm or 2.0 cm) guarantees precision through subtraction.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: The exact zero point cannot be seen, leading to random errors</p>
</div>
"""
    },
    {
        "id": 20,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 20,
        "question": "If an object's start aligns with 3.0 cm and its end aligns with 9.4 cm on a scale, what is its true length in millimetres?",
        "options": ["64 mm", "94 mm", "30 mm", "6.4 mm"],
        "correct": 0,
        "explanation": "Length in cm = 9.4 - 3.0 = 6.4 cm. Converting to mm: 6.4 x 10 = 64 mm.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Length in cm = 9.4 cm - 3.0 cm = 6.4 cm.</p>
    <p>2. Since 1 cm = 10 mm, multiply by 10.</p>
    <p>3. 6.4 cm x 10 mm/cm = 64 mm.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: 64 mm</p>
</div>
"""
    },

    # Challenge 3 (Q21 - Q30): Slides 9-13 topics
    {
        "id": 21,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 21,
        "question": "Which of the following notations strictly adheres to official SI writing rules?",
        "options": ["25ms", "25 cms.", "25 cm", "25CM"],
        "correct": 2,
        "explanation": "'25 cm' includes a single space between the number and unit, lowercase symbol, no plural 's', and no period.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Rule 1: A space must separate the numeric value from the symbol ('25 cm', not '25cm').</p>
    <p>2. Rule 2: Symbols never take a plural 's' ('cm', not 'cms').</p>
    <p>3. Rule 3: Symbols are written in lowercase ('cm', not 'CM').</p>
    <p>4. Rule 4: No full stop after a unit symbol unless at the end of a sentence.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: 25 cm</p>
</div>
"""
    },
    {
        "id": 22,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 22,
        "question": "Why is writing '10 ms' for ten metres scientifically misleading?",
        "options": ["Because 'ms' stands for milliseconds, a unit of time", "Because 'ms' stands for magnetic speed", "Because metres cannot be plural", "Because 10 is too large for metres"],
        "correct": 0,
        "explanation": "In SI conventions, 'ms' represents milliseconds ($10^{-3}$ seconds), not metres. Metre is always 'm'.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The SI prefix 'm' stands for milli ($10^{-3}$), and 's' stands for seconds.</p>
    <p>2. Therefore, 'ms' strictly denotes milliseconds.</p>
    <p>3. Adding an 's' to make 'm' plural alters the physical dimension from length to time!</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Because 'ms' stands for milliseconds, a unit of time</p>
</div>
"""
    },
    {
        "id": 23,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 23,
        "question": "How are tactile scales designed to assist visually challenged learners?",
        "options": ["They speak aloud through a microphone", "They feature raised, embossed dots and notched edges that can be felt by fingertips", "They glow in the dark", "They are made of heavy iron"],
        "correct": 1,
        "explanation": "Tactile rulers have embossed markings and Braille ridges enabling visually impaired students to measure length by touch.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Standard rulers rely on printed visual lines.</p>
    <p>2. Tactile scales emboss these lines into physical ridges and dots.</p>
    <p>3. Students run their fingertips along the edge to identify centimetre and millimetre marks independently.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: They feature raised, embossed dots and notched edges that can be felt by fingertips</p>
</div>
"""
    },
    {
        "id": 24,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 24,
        "question": "What is the recommended method to measure the length of a curved line drawn on paper?",
        "options": ["Break the scale into tiny pieces", "Lay a flexible thread along the curve, mark the ends, and measure the straightened thread on a ruler", "Estimate by counting squares by eye", "Soak the paper in water"],
        "correct": 1,
        "explanation": "A thread traces the exact curved path; when pulled straight against a scale, it yields the accurate length.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. A flexible thread is gently aligned with every bend and curvature of the line.</p>
    <p>2. The starting and ending points are marked on the thread with ink.</p>
    <p>3. The thread is then stretched straight along a standard centimetre ruler to read the distance.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Lay a flexible thread along the curve, mark the ends, and measure the straightened thread on a ruler</p>
</div>
"""
    },
    {
        "id": 25,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 25,
        "question": "What is a reference point in physics?",
        "options": ["A point that moves as fast as possible", "A fixed object or location used to specify the position and distance of another object", "The highest point on a mountain", "A point where friction is zero"],
        "correct": 1,
        "explanation": "A reference point (origin) is a stationary benchmark against which positions, displacements, and motions are measured.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. You cannot describe location without saying 'where from'.</p>
    <p>2. The 'where from' landmark is called the reference point.</p>
    <p>3. All measurements of distance, direction, and speed depend on the chosen reference frame.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: A fixed object or location used to specify the position and distance of another object</p>
</div>
"""
    },
    {
        "id": 26,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 26,
        "question": "Anish says: 'My home is 500 metres north of the post office.' What is the reference point in his statement?",
        "options": ["Anish's home", "The post office", "The school", "The northern horizon"],
        "correct": 1,
        "explanation": "The post office is the stationary origin from which the 500 m northward position is defined.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The position of Anish's home is being described.</p>
    <p>2. It is specified relative to the post office ('north of the post office').</p>
    <p>3. Therefore, the post office serves as the reference point.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: The post office</p>
</div>
"""
    },
    {
        "id": 27,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 27,
        "question": "When is an object scientifically said to be at rest?",
        "options": ["When it stops breathing", "When its position does not change with respect to a reference point over time", "When its speed exceeds 100 km/h", "When it is submerged in water"],
        "correct": 1,
        "explanation": "An object is at rest if its spatial coordinates remain unchanged relative to a chosen reference frame as time progresses.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Rest is the absence of position change over time.</p>
    <p>2. A desk in a classroom does not change its position relative to the floor or walls.</p>
    <p>3. Hence, it is in a state of rest relative to the classroom.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: When its position does not change with respect to a reference point over time</p>
</div>
"""
    },
    {
        "id": 28,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 28,
        "question": "When is an object scientifically defined as being in motion?",
        "options": ["When its position changes with respect to a reference point as time passes", "When it is exposed to sunlight", "When its mass increases", "When it becomes magnetic"],
        "correct": 0,
        "explanation": "Motion is strictly defined as a continuous change in position over time relative to a chosen reference point.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. If position changes from point A to point B as clock seconds advance, movement has occurred.</p>
    <p>2. This spatial displacement relative to an origin defines motion.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: When its position changes with respect to a reference point as time passes</p>
</div>
"""
    },
    {
        "id": 29,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 29,
        "question": "Two friends sit in adjacent seats on a moving bus. Are they in motion or at rest relative to each other?",
        "options": ["In rapid motion", "At rest, because their distance and direction from each other do not change", "They disappear", "They are in circular motion"],
        "correct": 1,
        "explanation": "Because the relative position between the two passengers is constant over time, they are at rest with respect to each other.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Both passengers travel at the identical velocity of the bus.</p>
    <p>2. The distance and angle between them remain perfectly fixed.</p>
    <p>3. Relative to each other's frame of reference, they are completely at rest.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: At rest, because their distance and direction from each other do not change</p>
</div>
"""
    },
    {
        "id": 30,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 30,
        "question": "Relative to a bystander standing on the roadside footpath, what is the state of a passenger inside a passing bus?",
        "options": ["At rest", "In motion, traveling with the speed of the bus", "Suspended in space", "Moving backwards"],
        "correct": 1,
        "explanation": "Relative to the fixed road, the passenger's position is changing continuously at the bus's cruising speed, so they are in motion.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The roadside bystander serves as the reference point.</p>
    <p>2. Every second, the distance between the bystander and the passenger changes.</p>
    <p>3. Therefore, relative to the bystander, the passenger is in motion.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: In motion, traveling with the speed of the bus</p>
</div>
"""
    },

    # Challenge 4 (Q31 - Q40): Slides 14-16 topics
    {
        "id": 31,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 31,
        "question": "What type of motion is executed by an apple falling straight down from a tree branch?",
        "options": ["Circular motion", "Linear (rectilinear) motion", "Oscillatory motion", "Periodic rotational motion"],
        "correct": 1,
        "explanation": "An apple falling under gravity moves along a straight vertical line, which is linear (rectilinear) motion.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Gravity pulls free-falling objects directly toward the center of the Earth.</p>
    <p>2. The path traced is a straight vertical line.</p>
    <p>3. Straight-line motion is classified as linear (or rectilinear) motion.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Linear (rectilinear) motion</p>
</div>
"""
    },
    {
        "id": 32,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 32,
        "question": "Which of the following is an everyday example of linear (rectilinear) motion?",
        "options": ["A child spinning on a merry-go-round", "Soldiers marching on a straight parade ground", "The swinging pendulum of a wall clock", "A stone whirled in a circle on a string"],
        "correct": 1,
        "explanation": "Marching soldiers advance in strict, straight parallel paths without turning, exemplifying rectilinear motion.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. A merry-go-round and whirled stone follow curved circular paths.</p>
    <p>2. A clock pendulum moves to-and-fro in oscillatory motion.</p>
    <p>3. Soldiers marching along a straight track move in linear motion.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Soldiers marching on a straight parade ground</p>
</div>
"""
    },
    {
        "id": 33,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 33,
        "question": "What type of motion is performed by a stone tied to a string and whirled overhead?",
        "options": ["Linear motion", "Circular motion", "Oscillatory motion", "Non-periodic motion"],
        "correct": 1,
        "explanation": "The stone traces a circular path around the hand while maintaining a constant radial distance equal to string length.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The string keeps the stone at a fixed distance from the center.</p>
    <p>2. The stone travels along the circumference of a circle.</p>
    <p>3. Movement along a circular path at constant radial distance is circular motion.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Circular motion</p>
</div>
"""
    },
    {
        "id": 34,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 34,
        "question": "Which component of a ceiling fan executes circular motion when the fan is switched on?",
        "options": ["The stationary ceiling mounting hook", "Points on the rotating blades", "The electrical switch on the wall", "The room floor"],
        "correct": 1,
        "explanation": "Every point on the fan blade moves in a circular path centered around the motor spindle.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The motor spindle acts as the fixed center of rotation.</p>
    <p>2. Any spot marked on a blade travels around that center at a constant radius.</p>
    <p>3. Hence, the blades execute circular motion.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Points on the rotating blades</p>
</div>
"""
    },
    {
        "id": 35,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 35,
        "question": "What type of motion is demonstrated by a swinging pendulum or a child on a playground swing?",
        "options": ["Linear motion", "Circular motion", "Oscillatory (to-and-fro) motion", "Random motion"],
        "correct": 2,
        "explanation": "Back-and-forth movement about a central equilibrium mean position is defined as oscillatory motion.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The swing or pendulum bob starts at the lowest central point (mean position).</p>
    <p>2. It swings forward to an extreme, stops, reverses through the center to the opposite extreme, and repeats.</p>
    <p>3. This to-and-fro movement across a central rest point is oscillatory motion.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Oscillatory (to-and-fro) motion</p>
</div>
"""
    },
    {
        "id": 36,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 36,
        "question": "When the string of a sitar or guitar is plucked, what kind of motion does it perform to produce sound?",
        "options": ["Linear motion across the room", "Oscillatory (vibrational) motion", "Circular motion around the neck", "Uniform translational motion"],
        "correct": 1,
        "explanation": "A plucked musical string vibrates rapidly to-and-fro across its resting position, which is oscillatory (vibratory) motion.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Plucking pulls the string away from its straight equilibrium line.</p>
    <p>2. Elastic tension pulls it back, causing it to overshoot and oscillate back and forth.</p>
    <p>3. These rapid oscillatory vibrations create acoustic sound waves in the air.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Oscillatory (vibrational) motion</p>
</div>
"""
    },
    {
        "id": 37,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 37,
        "question": "What is the defining characteristic of periodic motion?",
        "options": ["It only moves in straight lines", "It repeats its path after regular, fixed intervals of time", "It stops permanently after 10 seconds", "It creates light"],
        "correct": 1,
        "explanation": "Periodic motion is any motion that repeats itself in identical cycles over equal, regular intervals of time.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The period is the time taken to complete one full cycle.</p>
    <p>2. If every cycle takes the exact same duration (e.g., 60 seconds for a clock minute hand, 24 hours for Earth rotation), it is periodic.</p>
    <p>3. Both uniform circular and regular oscillatory motions are periodic.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: It repeats its path after regular, fixed intervals of time</p>
</div>
"""
    },
    {
        "id": 38,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 38,
        "question": "Which of the following motions is both circular AND periodic?",
        "options": ["A car slamming on emergency brakes", "The revolution of the tip of the second-hand on a clock", "A falling raindrop", "A football kicked across a field"],
        "correct": 1,
        "explanation": "The second-hand moves in a circle (circular) and completes each 360-degree revolution in exactly 60 seconds (periodic).",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The tip follows a circular path at constant radius (circular motion).</p>
    <p>2. It repeats its cycle every 60 seconds predictably (periodic motion).</p>
    <p>3. Therefore, it exhibits both circular and periodic motion simultaneously.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: The revolution of the tip of the second-hand on a clock</p>
</div>
"""
    },
    {
        "id": 39,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 39,
        "question": "A drill machine bit rotates rapidly to drill a hole into a wooden plank while simultaneously moving forward into the wood. What combined motions does it exhibit?",
        "options": ["Only linear motion", "Only circular motion", "Combined rotational (circular) and linear motion", "Oscillatory and random motion"],
        "correct": 2,
        "explanation": "The drill bit spins around its axis (rotational/circular) while advancing forward in a straight line (linear).",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Spinning around its central axis represents rotational motion.</p>
    <p>2. Penetrating straight forward into the plank represents linear motion.</p>
    <p>3. Real-world machinery frequently combines multiple types of motion.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Combined rotational (circular) and linear motion</p>
</div>
"""
    },
    {
        "id": 40,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 40,
        "question": "Which of the following correctly pairs an object with its primary type of motion?",
        "options": ["Marching soldier — Circular motion", "Struck tuning fork — Oscillatory motion", "Falling coconut — Oscillatory motion", "Clock pendulum — Linear motion"],
        "correct": 1,
        "explanation": "The prongs of a struck tuning fork oscillate to-and-fro rapidly, generating sound vibrations.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Marching soldiers execute linear motion.</p>
    <p>2. A falling coconut executes linear (free-fall) motion.</p>
    <p>3. A clock pendulum executes oscillatory motion.</p>
    <p>4. A struck tuning fork executes oscillatory (vibrational) motion.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Struck tuning fork — Oscillatory motion</p>
</div>
"""
    }
]

# Verify no latex
for q in quiz_questions:
    verify_no_latex(q['question'], f"Question {q['id']} question")
    for opt in q['options']:
        verify_no_latex(opt, f"Question {q['id']} option")
    verify_no_latex(q['explanation'], f"Question {q['id']} explanation")
    verify_no_latex(q['solution_html'], f"Question {q['id']} solution_html")

print(f"Verified {len(quiz_questions)} quiz questions with zero raw LaTeX.")

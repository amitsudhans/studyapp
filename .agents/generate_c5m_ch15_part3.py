# -*- coding: utf-8 -*-
"""Generate Slides 17 to 20 (40 Mastery Quiz Questions) for Chapter 15: Data Through Pictures"""

import re

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "tagline": "Mastery Challenge 1 • Raw Data, Tally Bundles & TV Survey Frequency Tables",
        "lecture": "",
        "content_html": "",
        "questions": [
            {
                "question": "What is the primary defining feature of raw data?",
                "options": [
                    "It has already been plotted on a finished bar graph",
                    "It is initial unorganized numbers collected directly from observations",
                    "It is always a set of exactly 100 percentages",
                    "It only contains numbers that have been rounded"
                ],
                "answer": 1,
                "hint": "Think of notes scribbled in a notebook before any sorting.",
                "explanation": "Raw data represents original, unorganized information collected directly from source observations before categorization.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. By definition, raw data consists of original, unprocessed observations.<br>2. Before data is arranged in tables or graphs, it is in 'raw' form."
            },
            {
                "question": "In standard tally mark notation, what does a diagonal line across four vertical lines (<s>||||</s>) represent?",
                "options": ["A group of 4 items", "A group of 5 items", "A group of 6 items", "A group of 10 items"],
                "answer": 1,
                "hint": "Count the four strokes plus the fifth crossing slash.",
                "explanation": "Four vertical strokes crossed by one diagonal slash represents a bundle of exactly 5 tally marks.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Four vertical lines = 4 units.<br>2. One crossing diagonal line = 1 unit.<br>3. Total bundle = 4 + 1 = 5 units."
            },
            {
                "question": "How many items are represented by three full tally bundles and two single marks (<s>||||</s> <s>||||</s> <s>||||</s> ||)?",
                "options": ["15 items", "17 items", "18 items", "12 items"],
                "answer": 1,
                "hint": "Multiply 3 bundles by 5, then add 2.",
                "explanation": "3 bundles × 5 = 15. Adding 2 single marks: 15 + 2 = 17 items.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 3 full bundles × 5 items/bundle = 15 items.<br>2. 2 individual strokes = 2 items.<br>3. Total count = 15 + 2 = 17 items."
            },
            {
                "question": "In the 35-classmate TV viewing survey, how many children watched TV for 1 hour?",
                "options": ["5 children", "8 children", "12 children", "6 children"],
                "answer": 2,
                "hint": "Look for the category with the highest frequency.",
                "explanation": "The frequency table records 12 children in the 1-hour viewing category.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. In the survey data: ½ hr = 5, 1 hr = 12, 1½ hrs = 8, 2 hrs = 6, >2 hrs = 4.<br>2. The 1-hour row has 12 children."
            },
            {
                "question": "How many total children watch TV for 1 hour or less per day in the 35-student survey?",
                "options": ["12 children", "17 children", "18 children", "25 children"],
                "answer": 1,
                "hint": "Add the counts for ½ hour and 1 hour.",
                "explanation": "5 (½ hr) + 12 (1 hr) = 17 children watch one hour or less.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Category ½ hour = 5 children.<br>2. Category 1 hour = 12 children.<br>3. Combined: 5 + 12 = 17 children."
            },
            {
                "question": "How many total children watch TV for more than 1 hour per day?",
                "options": ["17 children", "18 children", "20 children", "14 children"],
                "answer": 1,
                "hint": "Sum the categories: 1½ hrs, 2 hrs, and >2 hrs.",
                "explanation": "8 (1½ hrs) + 6 (2 hrs) + 4 (>2 hrs) = 18 children watch more than one hour.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Category 1½ hrs = 8.<br>2. Category 2 hrs = 6.<br>3. Category >2 hrs = 4.<br>4. Total = 8 + 6 + 4 = 18 children."
            },
            {
                "question": "What is the check sum of the frequencies for all 5 time intervals (5 + 12 + 8 + 6 + 4)?",
                "options": ["30", "35", "40", "50"],
                "answer": 1,
                "hint": "Add all 5 frequency numbers together.",
                "explanation": "5 + 12 + 8 + 6 + 4 = 35, matching the total number of surveyed classmates.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 5 + 12 = 17.<br>2. 17 + 8 = 25.<br>3. 25 + 6 = 31.<br>4. 31 + 4 = 35 total respondents."
            },
            {
                "question": "What percentage of the surveyed cohort of 35 children watch TV for more than 2 hours if 4 children are in that group?",
                "options": ["4/35 of the cohort", "12/35 of the cohort", "1/2 of the cohort", "35/4 of the cohort"],
                "answer": 0,
                "hint": "Write the count over the total surveyed population.",
                "explanation": "Exactly 4 out of the 35 surveyed children fall in the more than 2 hours category, represented as 4/35.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Count in category = 4.<br>2. Total population = 35.<br>3. Fraction = 4/35."
            },
            {
                "question": "Why must categories in a frequency table be mutually exclusive?",
                "options": [
                    "So that each student response is counted in exactly one category without overlap",
                    "So that the numbers are always multiples of 10",
                    "To ensure every category has the same number of students",
                    "To eliminate the need for tally marks"
                ],
                "answer": 0,
                "hint": "Consider what happens if someone fits into two categories at once.",
                "explanation": "Mutually exclusive categories ensure each observation belongs to one and only one group, preventing double counting.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 'Mutually exclusive' means categories do not overlap.<br>2. If categories overlapped, a single child could be counted twice, corrupting the survey sum."
            },
            {
                "question": "If 18 out of 35 children watch more than 1 hour of TV daily, is it True that more than half the children exceed 1 hour?",
                "options": [
                    "True (since half of 35 is 17.5, and 18 > 17.5)",
                    "False (since 18 is less than half)",
                    "Cannot be determined without knowing their ages",
                    "False because 35 is an odd number"
                ],
                "answer": 0,
                "hint": "Calculate half of 35.",
                "explanation": "Half of 35 is 17.5. Since 18 is greater than 17.5, more than half the children watch more than 1 hour daily.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Half of 35 = 35 ÷ 2 = 17.5.<br>2. Actual count = 18.<br>3. 18 > 17.5, so the statement is True."
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "tagline": "Mastery Challenge 2 • Pictograph Keys, Re-scaling & Traffic Observation Tallies",
        "lecture": "",
        "content_html": "",
        "questions": [
            {
                "question": "What is the primary function of a Key in a pictograph?",
                "options": [
                    "To lock the document so no one can edit it",
                    "To state how many physical units each picture symbol represents",
                    "To list the names of the students who drew the pictures",
                    "To specify the color of paint to use"
                ],
                "answer": 1,
                "hint": "Look for the scaling explanation.",
                "explanation": "The Key or Scale defines the numerical value that each individual icon symbol represents.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. In pictographs, symbols represent scaled quantities.<br>2. The Key provides the translation factor from symbols to real-world units."
            },
            {
                "question": "In a toy shop pictograph where 1 star = 5 items, how many board games are represented by 6 star icons?",
                "options": ["11 items", "25 items", "30 items", "60 items"],
                "answer": 2,
                "hint": "Multiply 6 by 5.",
                "explanation": "6 icons × 5 items per icon = 30 board games.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Number of icons = 6.<br>2. Scale per icon = 5.<br>3. Total = 6 × 5 = 30 board games."
            },
            {
                "question": "How many icons must be drawn to represent 40 sports gear items when the scale is 1 icon = 5 items?",
                "options": ["4 icons", "8 icons", "10 icons", "20 icons"],
                "answer": 1,
                "hint": "Divide 40 by 5.",
                "explanation": "40 items ÷ 5 items per icon = 8 icons.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Total items = 40.<br>2. Scale = 5.<br>3. Icons needed = 40 ÷ 5 = 8 icons."
            },
            {
                "question": "If the toy shop has 90 total items and changes its scale from 1 icon = 5 items to 1 icon = 10 items, how many icons are needed under the new scale?",
                "options": ["18 icons", "9 icons", "45 icons", "10 icons"],
                "answer": 1,
                "hint": "Divide 90 by 10.",
                "explanation": "90 items ÷ 10 items per icon = 9 icons.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Total items = 90.<br>2. New scale = 10.<br>3. Number of icons = 90 ÷ 10 = 9 icons."
            },
            {
                "question": "In the street traffic survey, 1 scooter symbol represents 3 two-wheelers. How many vehicles passed on Monday if 5 symbols were drawn?",
                "options": ["8 vehicles", "15 vehicles", "18 vehicles", "21 vehicles"],
                "answer": 1,
                "hint": "Multiply 5 by 3.",
                "explanation": "5 symbols × 3 vehicles per symbol = 15 two-wheelers.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Number of symbols = 5.<br>2. Scale = 3.<br>3. Total count = 5 × 3 = 15 vehicles."
            },
            {
                "question": "On Friday, 8 scooter symbols were recorded (scale: 1 symbol = 3 vehicles). How many vehicles passed on Friday?",
                "options": ["11 vehicles", "16 vehicles", "24 vehicles", "27 vehicles"],
                "answer": 2,
                "hint": "Multiply 8 by 3.",
                "explanation": "8 symbols × 3 vehicles per symbol = 24 two-wheelers.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Number of symbols = 8.<br>2. Scale = 3.<br>3. Total count = 8 × 3 = 24 vehicles."
            },
            {
                "question": "How many more two-wheelers passed on Friday (24) than on Wednesday (9)?",
                "options": ["12 vehicles", "15 vehicles", "18 vehicles", "21 vehicles"],
                "answer": 1,
                "hint": "Subtract 9 from 24.",
                "explanation": "24 - 9 = 15 more vehicles passed on Friday than on Wednesday.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Friday count = 24.<br>2. Wednesday count = 9.<br>3. Difference = 24 - 9 = 15 vehicles."
            },
            {
                "question": "What is the total number of two-wheelers observed across Monday (15), Wednesday (9), and Friday (24)?",
                "options": ["42 vehicles", "45 vehicles", "48 vehicles", "54 vehicles"],
                "answer": 2,
                "hint": "Add 15, 9, and 24.",
                "explanation": "15 + 9 + 24 = 48 two-wheelers in total.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 15 + 9 = 24.<br>2. 24 + 24 = 48 vehicles."
            },
            {
                "question": "If 1 icon represents 6 vehicles, how many icons represent 24 vehicles?",
                "options": ["2 icons", "3 icons", "4 icons", "6 icons"],
                "answer": 2,
                "hint": "Divide 24 by 6.",
                "explanation": "24 ÷ 6 = 4 full icons.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 24 vehicles ÷ 6 vehicles/icon = 4 icons."
            },
            {
                "question": "Under a scale of 1 icon = 6 vehicles, how is Monday's count of 15 vehicles represented?",
                "options": [
                    "2 full icons only",
                    "2 full icons plus 1 half-icon (6 + 6 + 3 = 15)",
                    "3 full icons",
                    "1 full icon plus 1 quarter-icon"
                ],
                "answer": 1,
                "hint": "15 = 12 + 3. Notice that 3 is half of 6.",
                "explanation": "15 ÷ 6 = 2 with a remainder of 3. Since 3 is half of 6, it is drawn as 2½ icons.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 2 full icons = 2 × 6 = 12.<br>2. 1 half-icon = 6 ÷ 2 = 3.<br>3. Total = 12 + 3 = 15 vehicles."
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "tagline": "Mastery Challenge 3 • 24-Hour Routines, Bar Graphs & Finger Strip Measurements",
        "lecture": "",
        "content_html": "",
        "questions": [
            {
                "question": "In a 24-hour daily routine, if a student sleeps 8 hours, what fraction of the full day is spent sleeping?",
                "options": ["1/4 of the day", "1/3 of the day", "1/2 of the day", "2/3 of the day"],
                "answer": 1,
                "hint": "Divide 8 by 24 and simplify the fraction.",
                "explanation": "8 ÷ 24 = 8/24 = 1/3 of the day.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Sleeping hours = 8.<br>2. Total hours in a day = 24.<br>3. Fraction = 8/24 = 1/3."
            },
            {
                "question": "In a vertical bar graph, which axis displays the numerical scale (such as hours or centimeters)?",
                "options": [
                    "The horizontal baseline",
                    "The vertical axis (Y-axis)",
                    "The chart title",
                    "The legend box"
                ],
                "answer": 1,
                "hint": "Think about which direction the bars rise.",
                "explanation": "In a standard vertical bar graph, the vertical axis (Y-axis) carries the numerical scale, determining the height of each bar.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Horizontal axis holds categorical labels.<br>2. Vertical axis holds the quantitative numerical scale."
            },
            {
                "question": "In the daily routine graph, School is 6 hours and Self-Study is 2 hours. How many total hours are dedicated to learning?",
                "options": ["4 hours", "6 hours", "8 hours", "10 hours"],
                "answer": 2,
                "hint": "Add 6 and 2.",
                "explanation": "6 + 2 = 8 hours total for educational activities.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. School hours = 6.<br>2. Self-study hours = 2.<br>3. Total learning hours = 6 + 2 = 8 hours."
            },
            {
                "question": "What is the check sum of all 5 daily routine activities: 8 (sleep) + 6 (school) + 2 (study) + 4 (play/food) + 4 (other)?",
                "options": ["20 hours", "22 hours", "24 hours", "26 hours"],
                "answer": 2,
                "hint": "A full day has 24 hours.",
                "explanation": "8 + 6 + 2 + 4 + 4 = 24 hours, accounting for the entire day.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 8 + 6 = 14.<br>2. 14 + 2 = 16.<br>3. 16 + 4 = 20.<br>4. 20 + 4 = 24 hours."
            },
            {
                "question": "What is the primary visual advantage of a bar graph over an icon list?",
                "options": [
                    "Bar graphs require using multiple paint colors",
                    "Bar heights allow immediate visual comparison of quantities without counting icons",
                    "Bar graphs can only be drawn on circular paper",
                    "Bar graphs do not need any numerical labels"
                ],
                "answer": 1,
                "hint": "Consider how quickly your eyes can compare two heights.",
                "explanation": "Bar graphs allow instantaneous visual comparison of quantities via bar heights without manual counting.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. With icons, you must count each symbol to find the value.<br>2. With bars, the relative height immediately communicates which category is larger."
            },
            {
                "question": "Why did students use flexible paper strips instead of stiff plastic rulers to measure their index fingers?",
                "options": [
                    "Paper strips bend smoothly along curved skin contours from base crease to tip",
                    "Plastic rulers are not allowed in mathematics class",
                    "Paper strips make fingers grow longer during measurement",
                    "Stiff rulers always break when measuring skin"
                ],
                "answer": 0,
                "hint": "Think about measuring along curved anatomical shapes.",
                "explanation": "Flexible paper strips conform smoothly along curved body contours, avoiding parallax and slippage errors.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Fingers have natural curves and creases.<br>2. Flexible strips mold along the surface for an accurate end-to-end measure."
            },
            {
                "question": "In the finger strip activity, Friend C's strip was 5.8 cm and Friend D's was 4.2 cm. What was the length difference?",
                "options": ["1.2 cm", "1.4 cm", "1.6 cm", "1.8 cm"],
                "answer": 2,
                "hint": "Subtract 4.2 from 5.8.",
                "explanation": "5.8 cm - 4.2 cm = 1.6 cm difference.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Longest strip = 5.8 cm.<br>2. Shortest strip = 4.2 cm.<br>3. Difference = 5.8 - 4.2 = 1.6 cm."
            },
            {
                "question": "Why must all paper strips be pasted starting from the exact same horizontal baseline?",
                "options": [
                    "To ensure that visual strip heights accurately reflect true finger lengths without offset bias",
                    "To prevent the paper strips from falling off the chart",
                    "So that all strips end up having the same length",
                    "To save glue during the activity"
                ],
                "answer": 0,
                "hint": "What happens if one runner starts 2 meters ahead in a race?",
                "explanation": "A common zero baseline ensures that the visible height of every strip is directly proportional to its true length.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. If strips started at different heights, a shorter strip placed higher would look taller.<br>2. A common baseline (height = 0) is required for valid comparative graphing."
            },
            {
                "question": "If Friend A has a finger length of 4.5 cm and Friend B has 5.0 cm, how much longer is Friend B's finger?",
                "options": ["0.3 cm", "0.5 cm", "1.0 cm", "0.2 cm"],
                "answer": 1,
                "hint": "Subtract 4.5 from 5.0.",
                "explanation": "5.0 cm - 4.5 cm = 0.5 cm (or 5 millimeters).",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 5.0 - 4.5 = 0.5 cm."
            },
            {
                "question": "How many millimeters are in 5.8 centimeters?",
                "options": ["58 mm", "580 mm", "5.8 mm", "0.58 mm"],
                "answer": 0,
                "hint": "Multiply centimeters by 10.",
                "explanation": "1 cm = 10 mm, so 5.8 cm × 10 = 58 mm.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 1 cm = 10 mm.<br>2. 5.8 × 10 = 58 mm."
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "tagline": "Mastery Challenge 4 • Canteen Waste Auditing, Observational Logic & 3D Nets",
        "lecture": "",
        "content_html": "",
        "questions": [
            {
                "question": "In the canteen food waste study, which menu day produced the highest waste (8 kg)?",
                "options": ["Monday (Sandwich)", "Tuesday (Paratha)", "Wednesday (Khichdi)", "Thursday (Puri-Sabzi)"],
                "answer": 3,
                "hint": "Look for the day with 8 kg on the notice board.",
                "explanation": "Thursday (Puri-Sabzi) produced 8 kg of waste, the highest of the week.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. The recorded values are: Mon = 4 kg, Tue = 7 kg, Wed = 3 kg, Thu = 8 kg, Fri = 5 kg.<br>2. The maximum is 8 kg on Thursday."
            },
            {
                "question": "Which menu day produced the lowest food waste (3 kg)?",
                "options": ["Monday (Sandwich)", "Wednesday (Khichdi)", "Thursday (Puri-Sabzi)", "Friday (Idli-Sambar)"],
                "answer": 1,
                "hint": "Look for the day with 3 kg.",
                "explanation": "Wednesday (Khichdi) produced only 3 kg of food waste, the lowest of the week.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 3 kg on Wednesday is the minimum value recorded across all five days."
            },
            {
                "question": "What was the total food waste across all five school days (4 + 7 + 3 + 8 + 5)?",
                "options": ["22 kg", "25 kg", "27 kg", "30 kg"],
                "answer": 2,
                "hint": "Add the five daily waste numbers.",
                "explanation": "4 + 7 + 3 + 8 + 5 = 27 kg total weekly waste.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 4 + 7 = 11.<br>2. 11 + 3 = 14.<br>3. 14 + 8 = 22.<br>4. 22 + 5 = 27 kg."
            },
            {
                "question": "If 1 kg of prepared food can feed 3 hungry children, how many children could be fed with the 27 kg of wasted food?",
                "options": ["54 children", "72 children", "81 children", "90 children"],
                "answer": 2,
                "hint": "Multiply 27 by 3.",
                "explanation": "27 kg × 3 children per kg = 81 children could have been fed.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Total waste = 27 kg.<br>2. Feeding rate = 3 children/kg.<br>3. 27 × 3 = 81 children."
            },
            {
                "question": "How much less food was wasted on Wednesday (3 kg) than on Tuesday (7 kg)?",
                "options": ["3 kg", "4 kg", "5 kg", "2 kg"],
                "answer": 1,
                "hint": "Subtract 3 from 7.",
                "explanation": "7 kg - 3 kg = 4 kg less waste on Wednesday.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Tuesday = 7 kg.<br>2. Wednesday = 3 kg.<br>3. Difference = 7 - 3 = 4 kg."
            },
            {
                "question": "In the courtyard picture logic puzzle, 4 children wear glasses and 6 wear backpacks. Which statement is False?",
                "options": [
                    "Backpack wearers exceed glasses wearers by 2",
                    "There are more children wearing glasses than backpacks",
                    "There are 6 children wearing backpacks",
                    "There are 4 children wearing glasses"
                ],
                "answer": 1,
                "hint": "Compare 4 with 6.",
                "explanation": "4 is less than 6, so claiming glasses wearers exceed backpack wearers is False.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Glasses = 4.<br>2. Backpacks = 6.<br>3. 4 < 6, so 'more glasses than backpacks' is False."
            },
            {
                "question": "If 5 children wear caps in a group of 12 children, how many children do NOT wear caps?",
                "options": ["5 children", "7 children", "8 children", "6 children"],
                "answer": 1,
                "hint": "Subtract 5 from 12.",
                "explanation": "12 - 5 = 7 children do not wear caps.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. Total cohort = 12.<br>2. Wearing caps = 5.<br>3. Not wearing caps = 12 - 5 = 7 children."
            },
            {
                "question": "What is a geometric net?",
                "options": [
                    "A fishing net used by mathematicians",
                    "A flat 2D pattern that can be folded to construct a 3D solid polyhedron",
                    "A computer network cable",
                    "A type of graph paper with circular dots only"
                ],
                "answer": 1,
                "hint": "Think of cutting paper and folding it into a box.",
                "explanation": "A geometric net is a flat 2D pattern of connected faces that folds along edges to enclose a 3D solid.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. In geometry, an unfolded flat layout of a solid's faces is called its net.<br>2. Folding along scored creases creates the 3D solid."
            },
            {
                "question": "How many equilateral triangular faces form the net of a regular icosahedron?",
                "options": ["12 faces", "18 faces", "20 faces", "30 faces"],
                "answer": 2,
                "hint": "The Greek prefix 'icosa' means twenty.",
                "explanation": "An icosahedron has exactly 20 congruent equilateral triangular faces.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 'Icosa' = 20.<br>2. A regular icosahedron has 20 triangular faces, 12 vertices, and 30 edges."
            },
            {
                "question": "What polygon shape forms the 12 faces of a regular dodecahedron net?",
                "options": ["Regular pentagons (5-sided)", "Equilateral triangles", "Squares", "Regular hexagons"],
                "answer": 0,
                "hint": "Think of 5-sided shapes.",
                "explanation": "A dodecahedron is composed of 12 regular pentagonal faces.",
                "solution_html": "<strong>Step-by-Step Derivation:</strong><br>1. 'Dodeca' = 12.<br>2. Each of the 12 faces is a regular 5-sided polygon (pentagon)."
            }
        ]
    }
]

print("=== VERIFYING PART 3 SLIDES ===")
assert len(slides_part3) == 4, f"Expected 4 slides, got {len(slides_part3)}"
for s in slides_part3:
    print(f"Slide {s['id']} ('{s['title']}'): {len(s['questions'])} questions")
    assert len(s['questions']) == 10, f"Slide {s['id']} must have 10 questions"
    for q in s['questions']:
        assert len(q['options']) == 4, f"Question must have 4 options: {q['question']}"
        assert 0 <= q['answer'] <= 3, f"Answer must be 0-3: {q['question']}"
        assert len(q['explanation']) > 10
        assert len(q['hint']) > 5
        assert len(q['solution_html']) > 15
print("Part 3 verified successfully!")

